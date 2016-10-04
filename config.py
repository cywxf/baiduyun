#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo

USER_QUEUE_LIST = []
WAIT_TIME = 3


MONGODB_HOST = "192.168.1.12"
MONGODB_PORT = 27017

#MONGODB_CLIENT = pymongo.MongoClient(MONGODB_HOST, MONGODB_PORT )
#DB = MONGODB_CLIENT["test"]
#
#COLLECTION_USER = DB["user"]
#COLLECTION_FOLLOW_FAN = DB["follow_fan"]
#COLLECTION_PUBSHARE = DB["pubshare"]

#print COLLECTION_USER
#print COLLECTION_FOLLOW_FAN
#print COLLECTION_PUBSHARE

URL_FOLLOW = "http://yun.baidu.com/pcloud/friend/getfollowlist?query_uk=%s&limit=25&start=%s"
URL_FAN = "http://yun.baidu.com/pcloud/friend/getfanslist?query_uk=%s&limit=25&start=%s"

COUNTSTART = 0
COUNTPERPAGE = 25

