import MySQLdb
import socket
import sys
import time,datetime
sys.path.append("/root/db_access_list/")
from  db_access_list import * #db_username db_password db_port of the db access, under /root/db_access_lista

class db():
    conn_src = False
    cursor_src = False
    db_ip = ""
    db_port = ""

    def __init__(self, source_ip, source_port = 6606, charset = "latin1"):
        try:
            socket.inet_aton(source_ip)
        except socket.error:
            print "illegal IP"

        self.db_ip = source_ip
        self.db_port = source_port
        self.charset = charset

        self.connect_mysql()

    def __del__(self):
      try:
        self.conn_src.close()
      except:
        pass

    def connect_mysql(self):
        source_db_host = self.db_ip
        source_db_user = db_username
        source_passwd  = db_password
        source_db_port = self.db_port
        source_db_charset = self.charset
        conn_retry = 0
        while self.conn_src == False and conn_retry <= 15:
            try:
                self.conn_src =MySQLdb.connect(host = source_db_host , user = source_db_user , passwd = source_passwd , db = 'mysql', port = source_db_port , connect_timeout = 2, charset = source_db_charset)
                self.cursor_src = self.conn_src.cursor()
                #print "Connect to %s success!" % (source_db_host)
            except:
                print "Connection to source DB %s failed" % ( source_db_host )
                time.sleep(1)
            conn_retry += 1
            if conn_retry > 1:
                print "Retry occurred!!! On DB with IP %s, Retry Counts %s" % (source_db_host,conn_retry)
        if conn_retry >= 16:
            sys.exit("connect to %s:%s failed" % (source_db_host,source_db_port))

    def run_sql(self, sql,one_row = False, param = False):
        try:
            self.cursor_src.execute("select 1;")
        except:
            print "Mysql Goneaway, reconnect (%s)" % self.db_ip
            self.conn_src = False
            self.connect_mysql()
        #while True:
        #  try:
        if param == False:
            self.cursor_src.execute(sql)
        else:
            self.cursor_src.execute(sql[0],sql[1])
        if one_row == True:
            return self.cursor_src.fetchone()
        else:
            return self.cursor_src.fetchall()
        #  except:
        #    print sql
        #    print "Mysql Goneaway, reconnect"
        #    self.conn_src = False
        #    self.connect_mysql()

    def commit(self):
        try:
            self.conn_src.commit()
        except:
            print "commit failed on DB %s" % self.db_ip
            self.conn_src = False
            self.connect_mysql()

    def rollback(self):
        try:
            self.conn_src.rollback()
        except:                                                                                                                                                                                 
            print "rollback failed on DB %s" % self.db_ip
            self.conn_src = False
            self.connect_mysql()
