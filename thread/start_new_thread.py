
#coding:utf-8
import time  
import thread  

# 1、  函数式：调用thread模块中的start_new_thread()函数来产生新线程。如下例：
def timer(no=0, interval=1):  
    cnt = 0  
    while cnt<10:  
        print 'Thread:(%d) Time:%s\n'%(no, time.ctime())  
        time.sleep(interval)  
        cnt+=1  
        print cnt
    thread.exit_thread()  
     
   
def test(): #Use thread.start_new_thread() to create 2 new threads  
    thread.start_new_thread(timer, (1,1))  
    thread.start_new_thread(timer, (2,2))  
   
if __name__=='__main__':  
    test()  
    
#测试结果如下，
#  Unhandled exception in thread started by 
# sys.excepthook is missing
# lost sys.stderr
# Unhandled exception in thread started by 
# sys.excepthook is missing
# lost sys.stderr

# 网上查出原因是不建议使用thread，然后我在pythonGUI中做了测试，
# 显然python是支持thread创建多线程的，在pydev中出错原因暂时不明。

