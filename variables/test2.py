# import time
# CONSTANT = 0

# def modifyConstant() : 
#     global CONSTANT 
#     print CONSTANT 
#     CONSTANT += 1
#     return
# if __name__ == '__main__' : 
#     modifyConstant() 
#     print CONSTANT
#     time.sleep(2)
#     print CONSTANT


a = 1
def external():
    global a
    a = 200
    print a
 
    b = 100
    def internal():
        # nonlocal b
        print b
        b = 200
        return b
 
    internal()def counter(start):
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
    print b
 
print external()