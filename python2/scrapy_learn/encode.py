#coding:utf-8
"""
Created on Wed Jul 20 12:59:33 2016

@author: kongwentao
"""
import sys
#需要提前pip install chardet
import chardet
string = "-------你好-------"

print sys.getdefaultencoding()

print string
#查看字符编码格式使用chardet
#这里的unicode编码不会因为设置的coding变化
code = chardet.detect(string)
code["daniel"]=u"孔文涛" #u'\u5b54\u6587\u6d9b' 
print code
print code['daniel']+"++++++++++++"

print "------------------这里中文字符转换---------------------------"
dan = code['daniel']
print dan,len(dan),type(dan)


#unidan = dan.encode("unicode")
print dan
print "_____________________"

#不能直接detect（dan）类型不兼容，detect无法识别，不知道具体原因
#print chardet.detect(dan)
udan = dan.encode("utf-8")
print udan + 'dan.encode("utf-8")'
print chardet.detect(udan)
print "+++++++++++++++++++++++++++++++++++++++++++"
print unicode(string,'utf-8')
print unicode(string,'gbk')

uni = string.decode("utf-8");
print uni



