#coding:utf-8
'''
Created on 2016年7月28日

@author: kongwentao
'''
import json

class User(object):
    def __init__(self, name):
        self.name = name

class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return obj.name
        return json.JSONEncoder.default(self, obj)

json_2 = {'user':User('orangle')}
json_1 = {'href': [u'/search/category/2/0/r1488'], 'name': [u'\u4e2d\u5173\u6751']}
print json.dumps(json_1, cls=UserEncoder)
