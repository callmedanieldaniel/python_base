import time

from global_var import GLOBAL_1,GLOBAL_2

def displayTest1():
    while True:
        print "GLOBAL_1,GLOBAL_2",GLOBAL_1,GLOBAL_2
        time.sleep(1.5)
        
displayTest1()