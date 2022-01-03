# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 16:26:12 2016

@author: kongwentao
"""
item = {'href': [u'/search/category/2/0/r1488'], 'name': [u'\u4e2d\u5173\u6751']}
print item
print type(item['name'][0])
uni = item['name'][0]
print uni#.encode('utf-8').decode('utf-8')
#with open 打开文件会自动关闭，不占用文件
print "-------------------------------------"
import os

#改变工作路径
#os.chdir(r'D:\scrapyWorkspace\ScrapyStudy\scrapy_dev')
#追加文件
with open('test.txt','a+') as f:
    for i in range(0,10):
        f.write(uni.encode('utf-8'))
        f.write("item")
        
        
with open('test.txt','a+') as f:
    print f.read()
    print f.tell()
    #返回一个整数,表示当前文件指针的位置(就是到文件头的比特数).
    
    #f.seek(偏移量,[起始位置])
    #用来移动文件指针。偏移量:单位:比特,可正可负
    #起始位置:0-文件头,默认值;1-当前位置;2-文件尾
    print "+++++++ f.seek(65,0)+++++++++"    
    f.seek(65,0)
    for i in range(0,10):
        print f.readline()
    f.truncate()
    print "--------------"
    print f.read()
    
#删除文件
os.remove('test.txt')


#读写模式：
# r只读,r+读写,w新建(会覆盖原有文件),a追加,b二进制文件
#常用读写模式
#如:'rb','wb','r+b'等等
#读写模式的类型有：
#rU 或 Ua 以读方式打开, 同时提供通用换行符支持 (PEP 278)
#w      以写方式打开，
#a      以追加模式打开 (从 EOF 开始, 必要时创建新文件)
#r+     以读写模式打开
#w+     以读写模式打开
#a+     以读写模式打开
#rb     以二进制读模式打开
#wb     以二进制写模式打开
#ab     以二进制追加模式打开
#rb+    以二进制读写模式打开
#wb+    以二进制读写模式打开
#ab+    以二进制读写模式打开
#W      若文件存在，首先要清空，然后重新创建文件
#a      把所有的数据追加到文件的尾部，即使seek指在其他的位置，如果文件不存在，则重新创建
