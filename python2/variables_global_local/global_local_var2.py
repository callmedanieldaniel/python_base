#coding:utf-8
def counter(start):
    count =[start]
    def internal():
        count[0] += 1
        return count[0]
    return internal
  
count = counter(0)
for n in range(10):
    print count()
# 1,2,3,4,5,6,7,8,9,10
  
count = counter(0)
print count()