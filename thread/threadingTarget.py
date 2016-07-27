#coding:utf-8
from threading import Thread    
import time
# from func import run_thread
var = 0
def run_thread(n,loop):    
    global var
    for i in range(loop): 
        var += n    
        print  var
        time.sleep(0.6)
     
t1 = Thread(target=run_thread,args=(100,10))#指定目标函数，传入参数，这里参数也是元组  
t2 = Thread(target=run_thread,args=(1,20))#指定目标函数，传入参数，这里参数也是元组  

print "start"
time.sleep(2)
t1.start()  #启动线程  
t2.start()