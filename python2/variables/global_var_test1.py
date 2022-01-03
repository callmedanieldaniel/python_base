
from global_var import *
import time
t1_v1 = 0
t1_v2 = 0

def modifyGlobal():
    global t1_v1
    global t1_v2
    t1_v1 = 1
    
    t1_v2 = t1_v2 + 9999

    for i in range(1,10):
        global GLOBAL_1 
        GLOBAL_1 += 10 
        
        global GLOBAL_2
        GLOBAL_2 = 111
        
        time.sleep(0.1)
        print "_",
        time.sleep(0.2)
    time.sleep(1)




def modifyGlobal2():
    global t1_v1
    global t1_v2
    t1_v1 = 1
    
    t1_v2 = t1_v2+ 9999
    for i in range(1,5):
        global GLOBAL_1 
        GLOBAL_1 += 10 
         
        global GLOBAL_2
        GLOBAL_2 = 222
        
        time.sleep(0.1)
        print "*",
    time.sleep(1)

# modifyGlobal()
# print t1_v1,t1_v2,GLOBAL_1,GLOBAL_2
# modifyGlobal2()
# print t1_v1,t1_v2,GLOBAL_1,GLOBAL_2
# time.sleep(100)

