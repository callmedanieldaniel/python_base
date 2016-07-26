
#coding=gbk
import time
import re
import lxml.html

f=open(r'E:\baidu.html','r')
resp=f.read()
f.close()
t1=time.clock()
for x in xrange(1000):
    title=re.search(r'<title>(.*?)</title>',resp)
print time.clock()-t1

content=resp.decode('gbk')
dom=lxml.html.document_fromstring(content)
t2=time.clock()
for x in xrange(1000):
    for item in dom.xpath('//title'):
        title=item.text_content()
print time.clock()-t2




        
from lxml import etree
doc = etree.HTML(content)
t3=time.clock()
for x in xrange(1000):
    for path in doc.xpath('//title'):
        title=path.text
print time.clock()-t3


# from pyque import PyQuery
# page = PyQuery(content,parser='html')
# t4=time.clock()
# for x in xrange(1000):
#     title=page('title').text()
# print time.clock()-t4