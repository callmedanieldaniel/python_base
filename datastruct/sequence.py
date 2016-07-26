#coding=utf-8
'''
Created on 2016年7月5日

@author: kongwentao
'''

#!/usr/bin/python
# Filename: seq.py


#shoplist = ['apple', 'mango', 'carrot', 'banana']
shoplist = ('apple', 'mango', 'carrot', 'banana')


# Slicing on a list
print 'Item 1 to 3 is', shoplist[1:3]
print 'Item 2 to end is', shoplist[2:]

print '-2 to -1',   shoplist[-2:-1]
print '-1 to 2',   shoplist[-1:2]
print '2 to -1',   shoplist[2:-1]

print 'all  is :', shoplist[:]

print "---------------------------------"
# Indexing or 'Subscription' operation
print 'Item 0 is', shoplist[0]
print 'Item 1 is', shoplist[1]
print 'Item 2 is', shoplist[2]
print 'Item 3 is', shoplist[3]
print 'Item -1 is', shoplist[-1]
print 'Item -2 is', shoplist[-2]

print "--------------------------------"
# Slicing on a string
name = 'swaroop'
print 'characters 1 to 3 is', name[1:3]
print 'characters 2 to end is', name[2:]
print 'characters 1 to -1 is', name[1:-1]
print 'characters start to end is', name[:] 

