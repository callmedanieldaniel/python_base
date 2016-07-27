#coding:utf-8
from threading import Thread   

from set_var import inc
from get_var import get

#这里的线程没生效，直接就启动了inc和get
#这里有一个错误:不能使用inc()
# t1 = Thread(target= inc(),args=())
#inc()是函数，他不是简单的给target一个名字，而是执行了inc()函数返回结果给target

t1 = Thread(target= inc,args=())#指定目标函数，传入参数，这里参数也是元组  
t2 = Thread(target= get,args=())#指定目标函数，传入参数，这里参数也是元组  
print "__________"

#没能启动
t1.start()  #启动线程  
t2.start()