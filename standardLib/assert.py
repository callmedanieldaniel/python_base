#coding=utf-8
'''
Created on 2016年7月7日

@author: kongwentao
'''
mylist =['item']
assert len(mylist) >= 1
#pop 把内容取出来，清空list
print '--',mylist,'--',mylist.pop(),'--',mylist

mylist.append("object")
assert len(mylist) >= 1
print mylist

print "------------------------------------"
i = []
i.append("object")

#``反引号可以完成repr相同的功能，取得对象的规范字符串表示
print `i`
print repr(i)