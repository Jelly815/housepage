# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:23:18 2019

@author: Jelly
"""
from function import FUNC_CLASS

db_conn = FUNC_CLASS()
# 取得user的id
#user_id = FUNC_CLASS.get_user_id('m1b414f0be20777c30e0423f441b09db8')
user_id = db_conn.get_user_id('1','m1b414f0be20777c30e0423f441b09db8')
for r in user_id:
    print(r)
    
# 取得user的搜尋紀錄    
#re_data = FUNC_CLASS.get_this_user_search(FUNC_CLASS,user_id)

'''
for _,record_data in enumerate(re_data):
    # 取得非user的相同的紀錄
    same_records = FUNC_CLASS.get_same_record(user_id,re_data[record_data])
    
    if same_records != None:
        for same_record in (same_records):
            print(same_record)
           # times_range = function.get_times_range(same_record['user_id'],re_data[record_data])
  '''          
