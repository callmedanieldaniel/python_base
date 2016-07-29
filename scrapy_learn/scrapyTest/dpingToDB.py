#coding:utf-8


from items import RegionItem

region = RegionItem()

region['name'] = [u'\u4e2d\u5173\u6751']
region['href'] = [u'/search/category/2/0/r1488']



print "-----",region
restr = str(region)
print "str:",restr

with open('db.txt','a+') as f:
    f.truncate()
    f.write(restr)
#     f.write(region['name'][0].encode('utf-8'))
#     f.write(":")
#     f.write(region['href'][0].encode('utf-8'))
#     f.write(",")
    
with open('db.txt','r') as f:
    print f.read()



    