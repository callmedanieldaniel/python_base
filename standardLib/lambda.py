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

print "_________________________triple lambda"
def triplevarLam(x):
    return lambda A,B : x*A+B 
compute = triplevarLam(10)
print compute(5,2)
