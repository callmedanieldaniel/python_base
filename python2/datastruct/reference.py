#coding=utf-8
'''
Created on 2016年7月5日

@author: kongwentao
'''


print 'Simple Assignment'
shoplist = ['apple', 'mango', 'carrot', 'banana']
#这里是ref 参考，类似于java中的引用
#两个指向的是同一个对象
mylist = shoplist # mylist is just another name pointing to the same object!

del mylist[0]
print shoplist
print mylist
print "-----------------------------"
#这里是复制了，不再是参考，指向不同的对象
mylist = shoplist[:]
del mylist[0]

print shoplist
print mylist

