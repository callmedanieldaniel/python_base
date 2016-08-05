#coding:utf-8
'''
Created on 2016年8月4日

@author: kongwentao
'''
import pymongo
from pymongo.auth import MECHANISMS

def Sasl_Plain_Conn():
    conn = pymongo.MongoClient(host="192.168.4.196",port=27017)
   
    db = conn["scrapy"]
    
#     ['PLAIN', 'MONGODB-CR', 'GSSAPI', 'MONGODB-X509']  'SCRAM-SHA-1'
#     db.authenticate(name="xdata",password="xdatadev",mechanism = 'MONGODB-X509')
    string = db.my_collection
    print string
#      //与以下两种方式等同
# >>> client = MongoClient(“localhost”, 27017)
# >>> client = MongoClient(“mongodb://localhost:27017/”)

Sasl_Plain_Conn()