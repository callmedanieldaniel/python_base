#coding=utf-8
'''
Created on 2016年7月5日

@author: kongwentao
'''

mstring = "hello world,i am daniel"
if mstring.startswith('hell'):
    print 'mstring is start with hell'
if 'a' in mstring:
    print 'a is in mstring'
if mstring.find('llo') != -1:
    print 'llo is in mstring'
print '------------------------------'

astring = '    123456543 21123321'
print astring
print astring.center(40)
print astring.rjust(40)
print astring.ljust(40,'#')
print astring.strip()
print astring.count('1')  

print '---------------------------------'
shoplist = ["apple","你好","watch","人"]
delimiter = '_*_'
print delimiter.join(shoplist)

