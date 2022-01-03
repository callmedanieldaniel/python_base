#coding=utf-8
'''
Created on 2016年7月5日

@author: kongwentao
'''
#每个Python模块都有它的__name__，如果它是'__main__'，这说明这个模块被用户单独运行，我们可以进行相应的恰当操作

if __name__ == "__main__":
    print "this fun is executed by itself"
else:
    print "fun is called by someone"
    
def sayhello():
    print "hello everyone"
version = '1.1'