#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project: keras-yolo3
@File: make_main_txt.py
@Time: 2022/3/14 17:07
@Author: wanghao
@Description: TODO
"""
# -*- coding:utf-8 -*-
import os
import random

train_percent = 0.8  # 训练集占数据的比例
val_percent = 0.15    # 验证集占数据的比例
test_percent = 0.05     # 测试集占数据集的比例

xmlfilepath = 'Annotations'
txtsavepath = 'ImageSets/Main'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)        # 图片数量
list = range(num)

train_num = int(num * train_percent)  # train的数量
test_num = int(num * test_percent)    # test的数量
val_num = int(num * val_percent)      # val的数量

trainval = random.sample(list, train_num + val_num)
train = random.sample(trainval, train_num)

ftest = open('ImageSets/Main/test.txt', 'w')
ftrain = open('ImageSets/Main/train.txt', 'w')
fval = open('ImageSets/Main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrain.close()
ftest.close()
fval.close()
