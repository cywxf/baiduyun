#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import *
import threading

def query(tbl,qStr):
    print "query"
    pass
    
def getUser(user):
    uk = 0
    follow_count = 0
    fans_count = 0

    while uk not in USER_QUEUE_LIST:
        
        queue_user = user.find_one({"flg" : "0"})
        print queue_user
        
        if queue_user is None:
            print "No User Data Found."
            break
        
        uk = queue_user["uk"]
        follow_count = queue_user["follow_count"]
        fans_count= queue_user["fans_count"]
      
        if  uk not in USER_QUEUE_LIST:
            # USER_QUEUE_LIST.append(uk)
            addQueue(uk)
            return (uk, follow_count, fans_count)
        else:
            print "No User Flg is refer to Resolve!Please wait..."
            time.sleep(WAIT_TIME)
    
    # print uk,follow_count,fans_count
    # print USER_QUEUE_LIST

    pass

def setUserFlg(user,uk,flg):
    print "uk=" ,uk,",flg=",flg
    user.update({"uk":uk}, {"$set": {"flg": flg}})    
    
    
def addQueue(uk):
    USER_QUEUE_LIST.append(uk)
    pass

def delQueue(uk):
    USER_QUEUE_LIST.remove(uk)
    pass



if __name__ == '__main__':
    query("","")