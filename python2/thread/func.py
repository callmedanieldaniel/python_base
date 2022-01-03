#coding:utf
'''
Created on 2016年7月27日

@author: kong-8wentao
'''
import time

def run_thread(n,loop):    
    var = 0
    for i in range(loop): 
        var += n    
        print  var
        time.sleep(0.6)