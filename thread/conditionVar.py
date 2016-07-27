#coding:utf-8
'''
Created on 2016年7月27日

@author: kongwentao
'''

#     例子中，在初始状态下，Consumer处于wait状态，
#     Producer连续生产（对x执行增1操作）5次后，notify正在等待的Consumer。
#     Consumer被唤醒开始消费（对x执行减1操作） 

# 总结一下:
# 1 join方法的作用是阻塞主进程无法执行join以后的语句,专注执行多线程,必须等待多线程执行完毕之后才能执行主线程的语句。
# 2 多线程多join的情况下,依次执行各线程的join方法,前一个结束之后,才能执行后一个。
# 3 无参数,则等待到该线程结束,才开始执行下一个线程的join。
# 4 设置参数后,则等待该线程N秒之后不管该线程是否结束，就开始执行后面的主进程。


import threading  
  
import time  
  
class Producer(threading.Thread):  
  
    def __init__(self, t_name):  
        threading.Thread.__init__(self, name=t_name)  

    def run(self):  
  
        global x  
        con.acquire()  

        if x > 0:  
            con.wait()  
        else:  
            for i in range(5):  
                x=x+1    
                print "producing..." + str(x)    
            con.notify()  
        print "producer:",x
        time.sleep(5)  
        con.release()  
  
   
class Consumer(threading.Thread):  
  
    def __init__(self, t_name):  
        threading.Thread.__init__(self, name=t_name)  
        
    def run(self):  
        global x    
        con.acquire()    
        if x == 0:   
            print 'consumer wait1'   
            con.wait()    
        else:   
            for i in range(5):   
                x=x-1   
                print "consuming..." + str(x)   
            con.notify()  
        time.sleep(5)  
        print "consumer:",x  
        con.release()  
  
   
  
con = threading.Condition()  
  
x=0  
  
print 'start consumer'  
  
c=Consumer('consumer') 
c1=Consumer("consumer") 
  
print 'start producer'  
  
p=Producer('producer')  
p1=Producer('producer')    
  
p.start()  
#这样会死锁
# p1.start()  
# c1.start()
c.start() 
 
p1.start()  
c1.start()
print "----------------"  
p.join(1)    
c.join(1) 
p1.join(1)    
c1.join(1)
  
print "end:",x  



