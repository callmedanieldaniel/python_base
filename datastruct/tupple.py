#coding=utf-8
'''
Created on 2016年7月5日
@author: kongwentao
'''
#元组和列表十分类似，只不过元组和字符串一样是 不可变的 即你不能修改元组。
#元组通过圆括号中用逗号分割的项目定义。
#元组通常用在使语句或用户定义的函数能够安全地采用一组值的时候，即被使用的元组的值不会改变。

person = ("我",'shi','da','hao','人','都','走')
pinfo = (person,'你','和','wo','是','friends')
print person #为什么这里乱码
for per in person:
        print per,
print "---------------------"   
print len('都') #都 的utf-8的存储方式，会被认为是三个字的长度
print len(u"都")#都 的unicode编码格式存储，认为是一个
 
print "---------------------"  
print "person[0][0]",person[0][0] 
print "person[1][1] ",person[1][1] 
 
print "---------------------"  
print 'pinfo[1]',pinfo[1]
print '',pinfo[0][4]
print 'pinfo[2]',pinfo[2]
print 'get a second degree matalist:',pinfo[0][2]
