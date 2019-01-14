# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:23:18 2019

@author: Jelly
"""
from function import FUNC_CLASS

func = FUNC_CLASS()

# 取得user的id
user_id = func.get_user_id('m1b414f0be20777c30e0423f441b09db8')

    
# 取得user的搜尋紀錄    
record_data = func.get_this_user_search(user_id)

for _,record in enumerate(record_data):
    # 取得非user的相同的紀錄
    same_records = func.get_same_record(user_id,record_data[record])
    print(same_records)
    if same_records != None:
        for same_record in (same_records):
            print(same_record)
           # times_range = function.get_times_range(same_record['user_id'],record_data[record])
       
