# Create your views here.
import sys
from common.db import db
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404,render_to_response
from django.template import RequestContext
import json
import time
#from django.contrib.auth.decorators import login_required
#import memcache
import json
import base64
import json
import MySQLdb
#from sa_stats.forms import *

#IP = "10.10.20.41"
IP = "10.10.16.11"
notice = "In LIVE mode now!!!"

#@login_required
def submit(request):
    if request.method == "POST":
        request_data = request.POST["request_data"]
        print request_data
        request_data = json.loads(base64.b64decode(request_data.encode('unicode-escape').decode()))
        print request_data
        type_id = request_data[0]
        nid     = request_data[1]
        param1  = request_data[2]
        param2  =  request_data[3]
        param3  =  request_data[4]
        param4  =  request_data[5]
        desc    =  request_data[6]

        #print desc, MySQLdb.escape_string(unicode(desc).encode('utf8'))

        #Process nid
        first_char = nid[0]
        if first_char == "A":
            nid_value = int("0x88080001",16)
        elif first_char == "B":
            nid_value = int("0x880A0001",16)
        elif first_char == "C":
            nid_value = int("0x880B0001",16)

        if "D" in nid:
            nid_value += int("0x00100000",16)
        if "E" in nid:
            nid_value += int("0x00200000",16)
        if "F" in nid:
            nid_value += int("0x00400000",16)


        #Check data
        param1 = param1.split(" ")[1]
        if len(param3) >=256 or len(param4) >= 256 or len(desc)>=256:
            return HttpResponse("Bad_Data param3:%s bytes param4:%sbytes desc:%sbytes" % (len(param3), len(param4), len(desc)))

        test_db = db(IP)
        sql = [u"""replace into im_db.im_notify_config_tab values(%s,%s,%s,%s,%s,%s,%s)""".encode("utf8") , [str(type_id).encode("utf8"),
                                                                                                          str(nid_value).encode("utf8"),
                                                                                                          param1.encode("utf8"),
                                                                                                          param2.encode("utf8"),
                                                                                                          param3.encode("utf8"),
                                                                                                          param4.encode("utf8"),
                                                                                                          desc.encode("utf8")
                                                                                                          ]]
        #sql = sql.encode("utf8")

        #print sql
        test_db.run_sql(sql, param = True)
        test_db.commit()

        return HttpResponse("Done")

#@login_required
def view_existing(request):
    if request.method == "GET":

        if "type" in request.GET:
            type_id = request.GET["type"]

        test_db = db(IP)
        sql = """select column_name from information_schema.columns where table_schema = "im_db" and table_name =  "im_notify_config_tab" order by ordinal_position; """
        sql_result = test_db.run_sql(sql)

        display_keys = []
        parameter_string = ""
        first_time = True
        for item in sql_result:
            display_keys.append(item[0])
            if first_time == True:
                parameter_string += "`%s`" % (item[0] )
                first_time = False
            else:
                parameter_string += "," + "`%s`" % (item[0] )

        #sql = "set names latin1"
        #test_db.run_sql(sql)
        sql = "select %s from im_db.im_notify_config_tab" % (parameter_string)
        if "type" in request.GET:
            sql += " where type = %s" % (type_id)


        game_id_dict = {0:"None", 4097 :"lan", 16385:"war3", 16386:"dota", 16387:"aoe", 16388:"bf", 16389:"cod4", 16390:"cs1.6", 16391:"l4d", 16392:"ra", 16393:"sc", 16394:"kf",                             
                                    16395:"sanguo", 16396:"nobu", 16397:"ddtank", 32769:"HoN", 32771 :"LoLSAM", 32773:"BlackShot", 32774:"LoLPH", 32775:"LoLTW", 32777:"texas", 32779:"7Hero",                            
                                    32781:"WinTexas", 32782:"HoNCIS", 32783:"PerfectWorld", 32784:"LDJ", 32785:"MstarTW", 32786:"LoLTH", 32787:"LoLVN", 32788:"PWEN", 32789:"DNF",                                        
                                    32790:"PBTH", 32791:"ZSG", 32792:"FO3TH", 32793:"FO3", 32794:"FO3VN", 32795:"FO3ID", 32796:"VHT", 32797:"Mstar", 32798:"HoNCN", 32799:"LoLID",                                        
                                    32800:"HoNTR", 32801:"ELSPH", 32802:"POE", 32803:"PB", 32804:"AVATW", 32805:"FCTW", 32811:"PBPH"}

        game_name_list = ["%s %s"%(game_id_dict[key],key) for key in game_id_dict.keys()]

        display_items = []
        if "type" not in request.GET or type_id != "new":
            sql_result = test_db.run_sql(sql)

            for item in sql_result:                                                                                                                                                                                           
                item_dict = dict()                                                                                                                                                                                            
                for i in range(len(display_keys)):                                                                                                                                                                            
                    if display_keys[i] in [ "param4", "param3", "desc"]:                                                                                                                                                      
                        item_dict[display_keys[i]] = unicode(item[i]).encode('latin-1')                                                                                                                                       
                    elif display_keys[i] == "nid":#nid => abcde                                                                                                                                                               
                        result = ""                                                                                                                                                                                           
                        nid = item[i]                                                                                                                                                                                         
                        nid_hex = hex(nid)                                                                                                                                                                                    
                        base   = nid_hex[5]                                                                                                                                                                                   
                        option = nid_hex[4]                                                                                                                                                                                   
                        print option
                        if base == "8":                                                                                                                                                                                       
                            result = "A"                                                                                                                                                                                      
                        elif base == "a":                                                                                                                                                                                     
                            result = "B"                                                                                                                                                                                      
                        elif base == "b":                                                                                                                                                                                     
                            result = "C"                                                                                                                                                                                      
                                                                                                                                                                                                                          
                        if option == "1":                                                                                                                                                                                     
                            result += "D"                                                                                                                                                                                     
                        elif option == "2":                                                                                                                                                                                   
                            result += "E"                                                                                                                                                                                     
                        elif option == "3":                                                                                                                                                                                   
                            result += "DE"                                                                                                                                                                                    
                        elif option == "4":                                                                                                                                                                                   
                            result += "F"                                                                                                                                                                                    
                        elif option == "5":                                                                                                                                                                                   
                            result += "DF"                                                                                                                                                                                    
                        elif option == "6":                                                                                                                                                                                   
                            result += "EF"                                                                                                                                                                                    
                        elif option == "7":                                                                                                                                                                                   
                            result += "DEF"                                                                                                                                                                                    
                        item_dict[display_keys[i]] = result                                                                                                                                                                   
                    elif display_keys[i] == "param1":#gameid => game name                                                                                                                                                     
                    #game_id_dict = {0:"None", 4097 :"lan", 16385:"war3", 16386:"dota", 16387:"aoe", 16388:"bf", 16389:"cod4", 16390:"cs1.6", 16391:"l4d", 16392:"ra", 16393:"sc", 16394:"kf", 
                    #                16395:"sanguo", 16396:"nobu", 16397:"ddtank", 32769:"HoN", 32771 :"LoLSAM", 32773:"BlackShot", 32774:"LoLPH", 32775:"LoLTW", 32777:"texas", 32779:"7Hero", 
                    #                32781:"WinTexas", 32782:"HoNCIS", 32783:"PerfectWorld", 32784:"LDJ", 32785:"MstarTW", 32786:"LoLTH", 32787:"LoLVN", 32788:"PWEN", 32789:"DNF", 
                    #                32790:"PBTH", 32791:"ZSG", 32792:"FO3TH", 32793:"FO3", 32794:"FO3VN", 32795:"FO3ID", 32796:"VHT", 32797:"Mstar", 32798:"HoNCN", 32799:"LoLID", 
                    #                32800:"HoNTR", 32801:"ELSPH", 32802:"POE"}
                    #game_name_list = ["%s %s"%(game_id_dict[key],key) for key in game_id_dict.keys()]                    
                        current_game_name = game_id_dict[item[i]] + " " + str(item[i])                                                                                                                                        
                        item_dict[display_keys[i]] = current_game_name                                                                                                                                                        
                    else:                                                                                                                                                                                                     
                        item_dict[display_keys[i]] = item[i]           
                display_items.append(item_dict)  
        else:#get the next available type id
             sql = "select max(type) + 1 from im_db.im_notify_config_tab"
             sql_result = test_db.run_sql(sql, one_row = True)
             new_type_id = sql_result[0]
             display_items  =  [{"type": new_type_id, "nid": "C", "param1": 0 , "param2": "0", "param3": """url, if need '%', use '%%' instead""", "param4": """content, if need display '%', use '%%' instead. the text in {} will be displayed in highlight.""","desc": "",}]
             current_game_name = "None"

        #print display_items
    
        if "type" in request.GET:#Modify page
            return render_to_response('notify_configure_app/modify_existing.html', {"notice": notice, "display_keys":display_keys , "display_items":display_items, "game_name_list":game_name_list, "current_game_name":current_game_name})
        else:#Summary page
            return render_to_response('notify_configure_app/view_existing.html', {"notice": notice, "display_keys":display_keys , "display_items":display_items})

