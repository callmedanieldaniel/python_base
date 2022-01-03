
import globalVar as gv
import time

def set(): 
    gv.set_mq_client(10) 
    print "------set mq_client in set.py------mq_client: " + str(gv.get_mq_client())
def inc():
    for i in range(10):
        gv.inc_db_handle(10)
        time.sleep(0.3)
        print gv.get_db_handle()