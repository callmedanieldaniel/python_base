#coding:utf-8

import scrapy

num = 10
mi=2.3E10-num
_plural=3-4j

print mi,_plural

#测试佛挡杀佛
longstring = '''This is a multi-line string. 
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''

print longstring

print "hello world ,first \
        second line ,\
        third"
        
print 'what\'s'         "your name"
print "what\'s"        "your name"

print longstring.istitle()
print '-------------'
st = '.'
print longstring.index(st)
print longstring.isupper()
print longstring.capitalize()

