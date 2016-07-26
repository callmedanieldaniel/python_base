#coding=utf-8
'''
Created on 2016年7月7日

@author: kongwentao
'''

#!/usr/bin/python
# Filename: list_comprehension.py

listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print listtwo 


def powersum(power , *args):
    ''' return the sum of args'''
    total = 0;
    for i in args:
        total += pow(i, power)
    return total
print powersum(2,3,4)
print powersum(2,10)


