import redis_mq  
import Queue     
q = Queue.Queue()
test_redis = redis_mq.redis_input(q, "10.10.50.187", [20011], 11)
test_redis.set_interest([['channel_db.user_recent_channel_tab','insert','update','delete'],])
test_redis.start()

while True:
    if q.empty() == False:
        print q.get()
