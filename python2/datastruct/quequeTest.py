#coding=utf-8
'''
Created on 2016年7月5日

@author: kongwentao
'''
marks = "marks"
print '(Initialized Student: %s)' % marks,
print '(Initialized Student: %s)' % marks


from Queue import Queue  

item = {'href': [u'/search/category/2/0/r1488'], 'regionName': [u'\u4e2d\u5173\u6751']}
que = Queue()
for i in range(10):
    que.put(item)

for i in range(14):
    print item(0)
    #     print que.get()[1]

