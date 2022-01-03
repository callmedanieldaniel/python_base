#coding=utf-8
'''
Created on 2016年7月5日

@author: kongwentao
'''
from class_person import Person

swaroop = Person('Swaroop')

swaroop.selfPop()
swaroop.personPop()

Person.population += 5
print swaroop.population,'------------'
# swaroop.population += 10
Person.population += 20
print swaroop.population
print Person.population

swaroop.ni = 10
print 'swaroop.ni:',swaroop.ni


print '--------------------------------------'
kalam = Person('Abdul Kalam')
kalam.sayHi()
kalam.selfPop()
kalam.personPop()
kalam.population += 1
print kalam.population


print '--------------------------------------'
swaroop.sayHi()
swaroop.selfPop()
swaroop.personPop()