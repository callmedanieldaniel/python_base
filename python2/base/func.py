#coding=utf-8
'''
Created on 2016年7月5日

@author: kongwentao
'''
#函数，局部函数和全局函数
def maxNum(a,b) :
    if a > b :
        print a,"is bigger"
    elif a == b :
        print a,"等于",b
    else :
        print b," is the max"
        
maxNum(4, 6)
maxNum(9, 9)
a = 9
b = 34
maxNum(a, b)
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++ "


#参数默认是3，可以在使用时修改重新赋值
#如果a是字符串，则打印times次a
#若a是数字，则做乘法a*times
def say(a,times):
    print a * times
    
say("hello", 1)
say("gogo ", 2)    
say(4 , 5)
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++ "

#名字关键字指定给某个参数赋值
#这样不用关心参数位置的先后

def func(a = 1,b = 2,c = 3):
    '''This is a function test.

    you can use a,b,c to assign a value to one or more.'''
    
    print "a: ", a, "b: ", b,"c: ",c
    if a>b:
        return "this is a"
    else:
        return "this is b"
    
print func(c=5)
print func(b=333, c=0)
print func()

print "||||||func.__doc__||||||||"
print func.__doc__ 
print "||||||||help(func)||||||"
help(func)
print "||||||||||||||"
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++ "

#它的首行以大写字母开始，句号结尾。第二行是空行，从第三行开始是详细的描述
