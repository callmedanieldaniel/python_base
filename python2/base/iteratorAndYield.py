#coding:utf-8
'''
Created on 2016年7月28日

@author: kongwentao
'''
import itertools

print "-----------------list build by []------------------------------"
# mylist 是一个可迭代的对象。
# 当你使用一个列表生成式来建立一个列表的时候，就建立了一个可迭代的对象:
mylist = [x*x for x in range(3)]
for i in mylist :
    print(i)



print "------------------generator build by ()-----------------------"
'''
看起来除了把 [] 换成 () 外没什么不同。但是，你不可以再次使用 for i in mygenerator ,
 因为生成器只能被迭代一次：先计算出0，然后继续计算1，然后计算4，一个跟一个的…
'''
# 生成器是可以迭代的，但是你 只可以读取它一次 ，因为它并不把所有的值放在内存中，它是实时地生成数据:
mygenerator  = (x*x for x in range(3))
for i in mygenerator  :
    print(i)
    
    
    
print "------------------yield Generator---------------------------"
# yield 是一个类似 return 的关键字，只是这个函数返回的是个生成器。
# 为了精通 yield ,你必须要理解：当你调用这个函数的时候，函数内部的代码并不立马执行 ，这个函数只是返回一个生成器对象
def yieldGenerator():
    mylist = range(3)
    for i in mylist :
        yield i*i

mygen = yieldGenerator()
print mygen

for i in mygen:
    print(i)
    

print "-----------------------use itertools----------------------------------------"
hourses = [1,2,3,4]

races = itertools.permutations(hourses)
print races

print list(itertools.permutations(hourses))
print list(itertools.permutations(hourses),2)


