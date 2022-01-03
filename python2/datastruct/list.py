#coding=utf-8
'''
Created on 2016年7月5日

@author: kongwentao
'''
shoplist = ["apple","你好","watch","人"]

print "the items i need buy"
for item in shoplist:
    print item,
print "\nlen is ",len(shoplist)
shoplist.append("bigCake")
print "after append one :",shoplist
shoplist.sort()
print "after sort:",shoplist
olditem0 = shoplist[0]
del shoplist[0]
print "ater del:",shoplist
print "the olditem0 : ",olditem0



    