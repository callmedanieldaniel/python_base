#coding=utf-8
'''
Created on 2016年7月5日

@author: kongwentao
'''

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
bn = {11: 1,  22 : 2, 33: 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print "a:",a["two"]
print 'b:',b["one"]
print 'c:',c["three"]
print "d:",d["one"]
print "e:",e["two"]  

print "a:",a.get("one")

#字典不按照输入的顺序保存，它只认key：value的格式
print "a",a
print "bn:",bn[22]

