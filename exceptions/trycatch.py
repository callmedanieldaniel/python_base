#coding=utf-8
'''
Created on 2016年7月5日

@author: kongwentao
'''
import sys


try:
    s = raw_input('Enter something --> ')
#使用快捷键ctrl+z 结束运行
except EOFError:
    print '\nWhy did you do an EOF on me?'
    sys.exit() # exit the program
except:
    print '\nSome error/exception occurred.'
    # here, we are not exiting the program

print 'Done' 

