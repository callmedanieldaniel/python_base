from global_var_test1 import *
from global_var_test2 import *

global t1_v1
global t1_v2
global GLOBAL_1
global GLOBAL_2

modifyGlobal()
print t1_v1,t1_v2,GLOBAL_1,GLOBAL_2
displayTest1()
print t1_v1,t1_v2,GLOBAL_1,GLOBAL_2
modifyGlobal2()
print t1_v1,t1_v2,GLOBAL_1,GLOBAL_2
time.sleep(100)