#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from config import MONGODB_HOST,MONGODB_PORT
from config import *
from utils import *
import pymongo
import time
import requests


def getFollow(uk, follow_count):
    try:
        user_list = []
        follow_fan_list = []
    
        user_agent  = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers     = { 'User-Agent' : user_agent }
        
        print uk
        loop_count = follow_count/COUNTPERPAGE
        if loop_count < follow_count:
            loop_count += 1

        for i in range(loop_count):
            url = URL_FOLLOW % (uk,i*COUNTPERPAGE)
            print url
            
            r = requests.get(url, headers =headers )        
            print r.status_code
            
            # print r.json()
            user_list = r.json()["follow_list"]
            print r.json()
        
        
        return (user_list, follow_fan_list)
        
        '''
        user
        {
        "uk" : 1953571457,
        "uname" : "V*\u7b71\u73a5",
        "avatar_url" : "http:\/\/himg.bdimg.com\/sys\/portrait\/item\/6c745e75.jpg",
        "intro" : "",
        "user_type" : "3",
        "is_vip" : 0,
        "follow_count" : 1,
        "fans_count" : 57,
        "pubshare_count" : 70,
        "album_count" : 0,
        "flg" : "0",
        "create_timestamp" : 0,
        "update_timestamp" : 0
        }

        follow_fan
        {
        "uk" : -1,
        "follow_fan_type" : 0,
        "follow_fan_uk" : 0,
        "flg" : "0",
        "create_timestamp" : 0,
        "update_timestamp" : 0
        }
        '''
    except:
        print("getFollow error!")

def addFollow(uk):
    pass

def getfan(uk):
    pass

def addfan(uk):
    pass

def main():
    # print "main"
    MONGODB_CLIENT = pymongo.MongoClient(MONGODB_HOST, MONGODB_PORT )
    DB = MONGODB_CLIENT["test"]

    COLLECTION_USER = DB["user"]
    COLLECTION_FOLLOW_FAN = DB["follow_fan"]
    COLLECTION_PUBSHARE = DB["pubshare"]

    (uk, follow_count, fans_count) = getUser(COLLECTION_USER)

    print "uk=" , uk
    # setUserFlg(COLLECTION_USER,uk,"1")



#    print COLLECTION_USER.find_one()
#    print COLLECTION_FOLLOW_FAN.find_one()
#    print COLLECTION_PUBSHARE.find_one()
#    print USER_QUEUE_LIST

    print USER_QUEUE_LIST
    delQueue(uk)
    print USER_QUEUE_LIST

    pass

if __name__ == '__main__':
    # main()
    # uk= 1953571457.0
    getFollow(int(1327787586.0),144)