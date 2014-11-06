'''
example

import sys,os
sys.path.append("/root/db_access_list/")
import redis_mq  
import Queue     
q = Queue.Queue()
test_redis = redis_mq.redis_input(q, "10.10.50.184", [20000,20001,20002], 7)
test_redis.set_interest([['game_db.game_startlog_tab','insert','update'],])
test_redis.start()


Return value from queue: already are python dict
'''




import sys,os
import redis
import Queue
import threading
from datetime import datetime
from datetime import time
from datetime import timedelta
import time
import json

class redis_auto_reconnect():
    def __init__(self, host, port, db):
        self.host = host
        self.port = port
        self.db   = db

    def conn(self):
        conn_retry = 0
        while True:
            try:
                self.redis_conn = redis.StrictRedis(host=self.host, port=self.port, db=self.db)
                break
            except:
                conn_retry += 1
                print "Connection to Redis %s:%s failed for %sth times, retry in 10 seconds" % ( self.host, self.port, conn_retry )
                time.sleep(10)
             
    def get(self, key):
        retry_count = 0
        while True:
            try:
                return self.redis_conn.get(key)
            except:
                self.conn()

    def exists(self, key):
        retry_count = 0
        while True:
            try:
                return self.redis_conn.exists(key)
            except:
                self.conn()

class redis_input(threading.Thread):
    
    def __init__(self, queue, ip, port_list, db, log_path = ""):
        self.log_path = log_path
        self.redis_conn = []
        for port_item in port_list:
            #self.redis_conn.append(redis.StrictRedis(host=ip, port=port_item, db=db))
            self.redis_conn.append(redis_auto_reconnect(host=ip, port=port_item, db=db))

        if os.path.exists( self.log_path ) == True:
            try:
                input = open(log_path, 'r')
                self.redis_current_date = input.readline().strip()
                self.redis_current_position = int(input.readline().strip())
                input.close()
            except:
                input.close()

                input = open(log_path +'.bak', 'r')
                self.redis_current_date = input.readline().strip()
                self.redis_current_position = int(input.readline().strip())
                input.close()

            print "Redis MQ info inited by file"
        else:#no previous file record, start reading redis from current posistion
            self.redis_current_date = datetime.now().strftime("%Y%m%d")
            self.redis_current_position = int(self.redis_conn[0].get( "s.%s" % (self.redis_current_date) ))
            print "Redis MQ info inited by REDIS"
        print self.redis_current_date,self.redis_current_position
        self.queue = queue

        threading.Thread.__init__(self)

    table_operation_list = []#e.g. [['table_1','insert','update'],...]
    def set_interest(self, table_operation_list):
        self.table_operation_list = table_operation_list
        self.table_list = [d[0] for d in table_operation_list]
        print 'set', self.table_operation_list
        print 'set', self.table_list
        
    def record_position(self):
        if self.log_path != "":                                                                                                                                                                                   
            output = open(self.log_path, 'w')                                                                                                                                                                     
            output.write(self.redis_current_date + "\n")                                                                                                                                                          
            output.write(str(self.redis_current_position) + "\n")                                                                                                                                                 
            output.close()


            output = open(self.log_path + ".bak", 'w') 
            output.write(self.redis_current_date + "\n")        
            output.write(str(self.redis_current_position) + "\n")        
            output.close() 

    def run(self):
            #if self.redis_conn[0].exists("s.%s" % (redis_latest_date)) == False:#date on 248 too fast
            #    redis_latest_date = (datetime.strptime(redis_latest_date,"%Y%m%d") + timedelta(days = -1)).strftime("%Y%m%d")
            #redis_latest_position = self.redis_conn[0].get( "s.%s" % (redis_latest_date) )
            #run from current to latest
            while True:
                start = self.redis_current_position
                #print "s.%s" % (self.redis_current_date)
                stop  = int( self.redis_conn[0].get("s.%s" % (self.redis_current_date)) )
                print "run at date %s from %s to %s" % (self.redis_current_date, start, stop)
                for i in range(start, stop + 1):
                    pass
                    got_it = False
                    try_count = 0
                    while got_it == False:
                        for redis_instance_number in range(len(self.redis_conn)):
                            if self.redis_conn[redis_instance_number].exists( "v.%s.%s" % (self.redis_current_date, i) ):
                                got_it = True
                                json_string = self.redis_conn[redis_instance_number].get( "v.%s.%s" % (self.redis_current_date, i) )
                                json_result = json.loads(json_string)
                                table_name = str(json_result['table'])
                                if table_name in self.table_list:
                                    table_index = self.table_list.index(table_name)
                                    command = str(json_result['command'])
                                    if command in self.table_operation_list[table_index]:
                                        self.queue.put(json_result)
                                        #if command in ['insert','update']:
                                        #    print 'new row for table: %s command %s' % (table_name, command)
                                        #    for i in range(len(json_result['newrow'])):
                                        #        print i, json_result['newrow'][str(i)]
                                        #if command in ['update', 'delete']:
                                        #    print 'old row for table: %s command %s' % (table_name, command)
                                        #    for i in range(len(json_result['oldrow'])):
                                        #        print i, json_result['oldrow'][str(i)]
                        if got_it == False:
                            print "NOT_FOUND, try again v.%s.%s" % (self.redis_current_date, i)
                            try_count += 1
                            time.sleep(0.1)
                        if try_count > 10:
                            "Failed to find v.%s.%s" % (self.redis_current_date, i)
                            break
                self.redis_current_position = stop + 1
                #record current position
                self.record_position()
                #test loop condition
                #if self.redis_current_date < redis_latest_date:
                if start >= stop:
                    next_day =  (datetime.strptime(self.redis_current_date,"%Y%m%d") + timedelta(days = 1)).strftime("%Y%m%d")
                    if self.redis_conn[0].exists("s.%s" % (next_day)) == True:
                        print "goto next day because start = %s and stop = %s" % (start, stop) 
                        self.redis_current_date = (datetime.strptime(self.redis_current_date,"%Y%m%d") + timedelta(days = 1)).strftime("%Y%m%d")
                        self.redis_current_position = 1
                    
    job_queue = ""
    redis_conn = []

    redis_current_date = ""
    redis_current_position = ""
    game_id = 32782;
