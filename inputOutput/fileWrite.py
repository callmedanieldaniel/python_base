#coding=utf-8
'''
Created on 2016年7月5日

@author: kongwentao
'''
poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
        use Python!
'''
f = file('test.txt','a')
f.write(poem)
print f
f.write('this is for append')
f.close()

out = file("test.txt")
while True:
    line = out.readline()
    if len(line) == 0 :
        print "end line"
        break
    else:
        print line
out.close()


