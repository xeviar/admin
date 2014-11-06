import sys
sys.path.append("/root/db_access_list")

from db import db

gi = pygeoip.GeoIP('/usr/share/GeoIP/GeoIP.dat', pygeoip.MEMORY_CACHE)
log_db_slave = db("10.10.50.192")

def get_country(IP):
    try:
        socket.inet_aton(IP)
        return gi.country_code_by_name(IP)
    except:
        return "ZZ"

def test_changed_password(uid, timestamp, display_info = False):
    sql = '''select 1 from log_db.user_change_password_tab where uid = %s limit 1''' % (uid, timestamp)
    sql_result = log_db_slave.run_sql(sql)
    if display_info == True:
        print sql
        print sql_result

    if sql_result is None or len(sql_result) == 0 :                                                                                                                                                                       
        if display_info == True:                                                                                                                                                                                          
            print "Not found, return False"                                                                                                                                                                               
        return False                                                                                                                                                                                                      
    else:                                                                                                                                                                                                                 
        if display_info == True:                                                                                                                                                                                          
            print "Found, return True"                                                                                                                                                                                    
        return True             
