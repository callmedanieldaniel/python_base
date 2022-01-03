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
