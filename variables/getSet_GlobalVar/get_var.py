#!/usr/bin/env python2.7 

import globalVar as gv
import time

def get(): 
    for i in range(10):
        print "------get get_db_handle in get.py------mq_client: " + str(gv.get_db_handle())
        time.sleep(0.51)