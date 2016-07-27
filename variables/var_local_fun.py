#coding:utf-8
# globals()
# global 和 globals() 是不同的，global 是关键字用来声明一个局部变量为全局变量。globals() 和 locals() 提供了基于字典的访问全局和局部变量的方式
# 
# 比如：如果函数1内需要定义一个局部变量，名字另一个函数2相同，但又要在函数1内引用这个函数2。

def var():
    pass
 
def f2():
    var = 'Just a String'
    f1 = globals()['var']
    print var
    return type(f1)
 
print f2()

print "----------------------"



# 本文实例讲述了python通过函数属性实现全局变量的方法。分享给大家供大家参考。具体分析如下：
# 
# python的函数可以定义属性，而且是全局的，这个非常好用，例如用于数字累加，你不用专门去定义一个全局变量，使用函数的属性即可。

def add(x=1):
    try:
        add.sum += x
    except AttributeError:
        add.sum = x
    return add.sum
print add(3)
print add(4)
print add(10)

class Ax(object):
    def __init__(self, val=0):
        self.sum = val
      
    def __call__(self, x=1):
        self.sum += x
        return self.sum

print add 
print add(3)
print add(4)
print add(10)

