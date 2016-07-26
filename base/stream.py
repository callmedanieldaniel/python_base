#coding:utf-8
'''
Created on 2016年7月4日

@author: kongwentao
'''
from __builtin__ import range


number = 23

flag = True
def juedge():
    while flag:
        
            guess = raw_input('Enter an integer : ')
            
           
            if guess.isdigit():
                loopnum = int(guess)
                print 'this is a NUM:',guess
                if loopnum < number :
                    for i in range(1,loopnum):
                        print i
                        
            elif guess == "exit":
                print 'exit already' # Another block
                break
            elif guess == "continue" :
                print "before continue"
                continue
                print "after continue"
            else:
                print 'this is string' ,guess
                # you must have guess > number to reach here
            


print 'this is a juedge'           
juedge()