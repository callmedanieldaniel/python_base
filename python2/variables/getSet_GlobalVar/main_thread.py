#coding:utf-8
from threading import Thread   

from set_var import inc
from get_var import get

num =0
def increase():
    global num
    print num    
t1 = Thread(target= inc(),args=())#指定目标函数，传入参数，这里参数也是元组  
t2 = Thread(target= get(),args=())#指定目标函数，传入参数，这里参数也是元组  
print "__________"

t1.start()  #启动线程  
t2.start()