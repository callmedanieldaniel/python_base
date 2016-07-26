#coding=utf-8
'''
Created on 2016年7月5日

@author: kongwentao
'''
import os
import time

source = 'E:\\pytest\\hello.txt'
targetdir ='E:\\pytest\\'
today = targetdir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
    print 'succed mkdir %s' % today

target = today + now + '.zip'

#这是linux下的压缩命令，windows不适用
zip_command = "WinRAR.exe a %s %s " %(target , ''.join(source)) 

print zip_command
if os.system(zip_command) == 0 : 
    print "zip success to :%s" % target
else:
    print 'failed'


