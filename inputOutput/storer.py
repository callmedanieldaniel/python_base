#coding=utf-8
'''
Created on 2016年7月6日

@author: kongwentao
'''

import cPickle as cp

listfile = "hello.txt"
lista = ['apple','banana','orange']

inout = file(listfile,'a')
cp.dump(lista, inout, protocol=0)
inout.close()


while True:
    f = file(listfile)
    storedlist = cp.load(f)
    print storedlist