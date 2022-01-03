#coding:utf-8
'''
Created on 2016年7月26日

@author: kongwentao
'''
#global.py 
class GlobalVar: 
    db_handle = 0 
    mq_client = 0 
def set_db_handle(db): 
    GlobalVar.db_handle = db 
def inc_db_handle(num):
    GlobalVar.db_handle += num
def get_db_handle(): 
    return GlobalVar.db_handle

 
def set_mq_client(mq_cli): 
    GlobalVar.mq_client = mq_cli 
def inc_mq_client(num):
    GlobalVar.mq_client += num
def get_mq_client(): 
    return GlobalVar.mq_client