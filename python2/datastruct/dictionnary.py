#coding=utf-8
'''
Created on 2016年7月5日

@author: kongwentao
'''
aboy = {
       "name"   : "daniel",
       "age"    :   13 ,
       "city"   : "beijing",
       }

print aboy["name"]
aboy["height"] = 188
print aboy
print "%s's height is %s" % (aboy["name"], aboy["age"])
del aboy["city"]

for key , value in aboy.items():
    print "%s : %s" % (key, value)
    
