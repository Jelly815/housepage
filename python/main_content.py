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
#user_unid = 'm8456fba48ba8c14bdd683e92c7414dc8'

func = FUNC_CLASS(user_unid)

users_items = []
recommand_items = []
unique_items = []

# 取得A的搜尋紀錄
record_data = func.get_this_user_search()
if len(record_data['often_record']) > 1:
    for key,record in record_data.items():
        if record and key == 'last_record' and record[0] in record_data['often_record']:
            continue
        elif record:
            for record_val in record:
                user_items_dict = []
                others_user_items_dict = []
                times_range_items = []
                users_items2 = []

                # 取得A(喜愛)的物件(瀏覽時間大於5秒,瀏覽次數大於1or有加入最愛)
                times_range_items       = func.get_times_range_items(user_unid,record_val)

                if times_range_items:
                    user_items_dict = times_range_items
                    users_items.extend(times_range_items)
users_items = list(set(users_items))

####### 取得A(喜愛)的物件，找到相似內容的房子 #######
times_range_items_not = func.get_this_user_content(users_items)

recommand_items.extend(times_range_items_not)
recommand_items = list(set(recommand_items))

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