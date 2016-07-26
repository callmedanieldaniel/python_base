#coding=utf-8
'''
Created on 2016年7月7日

@author: kongwentao
'''
def make_repeater(n):
    return lambda s: s*n

twice = make_repeater(2)

print twice('word')
print twice(5) 
