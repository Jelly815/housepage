# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:23:18 2019

@author: Jelly
"""
import function

# 取得user的id
user_id = function.get_user_id('m1b414f0be20777c30e0423f441b09db8')

# 取得user的搜尋紀錄    
re_data = function.get_this_user_search(user_id)
print(re_data)

for _,record_data in enumerate(re_data):
    same_records = function.get_same_record(user_id,re_data[record_data])
    
    if same_records != None:
        for same_record in (same_records):
            print(same_record)