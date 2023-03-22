# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:23:18 2019

@author: Jelly
"""
from function import FUNC_CLASS
import sys
import setting
import random

user_unid = sys.argv[1]
#user_unid = 'm185ccab81019a39cba16f666f070bb83'

func = FUNC_CLASS(user_unid)

users_items = []
recommand_items = []
unique_items = []

####### 取得A(不喜愛)的物件，找到相同記錄、相同在意項目的人 #######
times_range_items_not = func.get_this_user_no_search()

# 找到相似記錄相似者喜歡的物件給他
recommand_items.extend(times_range_items_not)

# 取得A曾經搜尋過的條件
user_all_record = func.get_user_all_record()
recommand_items = func.get_user_all_record_items(user_all_record,recommand_items)

# 檢查是否有已經close的物件，若有則取相似的物件替換
if recommand_items:
    recommand_items     = func.check_close(recommand_items)

# 隨機取5個物件出來
if len(recommand_items) > 0 and len(recommand_items) < setting.random_num:
    print(random.sample(recommand_items, len(recommand_items)))
elif len(recommand_items) > 0:
    print(random.sample(recommand_items, setting.random_num))
else:
    print(users_items)