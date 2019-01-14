# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:23:18 2019

@author: Jelly
"""
from function import FUNC_CLASS
#import sys

#user_unid = sys.argv[1]
user_unid = 'm199cdc39ee6e65811960a187ccf1fcb9'

func = FUNC_CLASS()

# 取得user的id
user_id = func.get_user_id(user_unid)


# 取得user的搜尋紀錄
record_data = func.get_this_user_search(user_id)

for _,record in enumerate(record_data):
    # 取得非user的相同的紀錄
    same_records = func.get_same_record(user_id,record_data[record])

    if same_records != None:
        for same_record in (same_records):
            # 取得瀏覽物件的時間區間(單位:秒)
            times_range = func.get_times_range(same_record['user_id'],record_data[record])

