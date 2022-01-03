#!/usr/bin/python3
# coding=utf-8

# 第一个注释
# 第二个注释
from sklearn import datasets
boston = datasets.load_boston()
X = boston.data[:,5]#使用一个特征，注意更改此处使用boston房价数据集的13个特征或其他特征测试效果
y = boston.target

boston.data[:,9]