# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:23:18 2019

@author: Jelly
"""
from function import FUNC_CLASS
import sys
import setting
import random
from collections import defaultdict

user_unid = sys.argv[1]
#user_unid = 'mc741ce94208d215dc1a80e40c5456cf1'

func = FUNC_CLASS()

users_items = []
recommand_items = []
unique_items = []

####### 取得A(喜愛)的物件，找到相似內容的房子 #######
times_range_items_not = func.get_this_user_content(user_unid)

recommand_items.extend(times_range_items_not)
recommand_items = list(set(recommand_items))

# 檢查是否有已經close的物件，若有則取相似的物件替換
if recommand_items:
    recommand_items     = func.check_close(user_unid,recommand_items)

# 隨機取5個物件出來
if len(recommand_items) > 0 and len(recommand_items) < setting.random_num:
    print(random.sample(recommand_items, len(recommand_items)))
elif len(recommand_items) > 0:
    print(random.sample(recommand_items, setting.random_num))
else:
    print(users_items)