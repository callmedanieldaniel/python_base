#coding:utf-8
'''
Created on 2016年7月28日

@author: kongwentao
'''

# Python中的对象之间赋值时是按引用传递的，如果需要拷贝对象，需要使用标准库中的copy模块。
# 1. copy.copy 浅拷贝 只拷贝父对象，不会拷贝对象的内部的子对象。
# 2. copy.deepcopy 深拷贝 拷贝对象及其子对象
# 区别就在于在a中有另外一个对象或者list时，c = copy.copy(a) 并没有对[a,b]复制，只是引用了一下

import copy as cp

a = [1, 2, 3, 4, ['a', 'b']] #原始对象

b = a #赋值，传对象的引用
c = cp.copy(a)
d = cp.deepcopy(a) #对象拷贝，深拷贝

a.append(5) #修改对象a
a[4].append('c') #修改对象a中的['a', 'b']数组对象

print('a = ', a)
print 'b = ', b
print 'c = ', c
print 'd = ', d


# 输出结果：
# a = [1, 2, 3, 4, ['a', 'b', 'c'], 5]
# b = [1, 2, 3, 4, ['a', 'b', 'c'], 5]
# c = [1, 2, 3, 4, ['a', 'b', 'c']]
# d = [1, 2, 3, 4, ['a', 'b']]


