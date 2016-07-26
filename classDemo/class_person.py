#coding=utf-8
'''
Created on 2016年7月5日

@author: kongwentao
'''
class Person:
    '''Represents a person.'''
    population = 0

    def __init__(self, name):
        '''Initializes the person's data.'''
        Person.name = name
        print '(Initializing %s)' % Person.name

        # When this person is created, he/she
        # adds to the population
        Person.population += 1

    def __del__(self):
        '''I am dying.'''
        print '%s says bye.' % self.name
 
        Person.population -= 1
 
        if Person.population == 0:
            print 'I am the last one.--%s' % self.name
        else:
            print 'There are still %d people left.--%s' % (Person.population,self.name)

    def sayHi(self):
        '''Greeting by the person.

        Really, that's all it does.'''
        print 'Hi, my name is %s.' % self.name

    def selfPop(self):
        '''Prints the current population.'''
        if self.population == 1:
            print 'I am the only person here.'
        else:
            print 'We have %d population here.' % self.population

    def personPop(self):
        '''Prints the current population.'''
        if Person.population == 1:
            print 'I am the only person here.'
        else:
            print 'We have %d  person ++++.' % Person.population


