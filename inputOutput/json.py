# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 17:39:11 2016

@author: kongwentao
"""
#json 主要包含四个方法： 
#    dump和dumps（从Python生成JSON），
#    load和loads（解析JSON成Python的数据类型）
#    dump和dumps的唯一区别是dump会生成一个类文件对象，dumps会生成字符串，
#    同理load和loads分别解析类文件对象和字符串格式的JSON
import json 
dic = { 'str': 'this is a string', 'list': [1, 2, 'a', 'b'], 'sub_dic': { 'sub_str': 'this is sub str', 'sub_list': [1, 2, 3] }, 'end': 'end' } 
json.dumps(dic)