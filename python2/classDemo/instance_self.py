#coding=utf-8
'''
Created on 2016年7月5日

@author: kongwentao
'''
from class_self import Person

swaroop = Person('Swaroop')

swaroop.selfPop()
swaroop.personPop()

Person.population += 5
print swaroop.population,'------------'
print Person.population,'------------'
# swaroop.population += 10
Person.population += 20
print swaroop.population
print Person.population

swaroop.ni = 10
print 'swaroop.ni:',swaroop.ni


print '------------&&&&&&&&&&&&&&&&&&&&&&&&&------------------'
kalam = Person('Abdul Kalam')
kalam.sayHi()
kalam.selfPop()
kalam.personPop()

Person.population = 100
kalam.population += 1
print '------------------------after self.population +1 --------------'
kalam.selfPop()
print kalam.population
kalam.personPop()

print '--------------------------------------'
swaroop.selfPop()
swaroop.personPop()
print "<><>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"