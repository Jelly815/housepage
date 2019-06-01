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
#user_unid = 'cca0a53df7abc791c9e61742a7acc8333'

func = FUNC_CLASS()

users_items = []
recommand_items = []
unique_items = []
# 取得A的搜尋紀錄
record_data = func.get_this_user_search(user_unid)

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
                    #user_items_dict.append(times_range_items)
                    user_items_dict = times_range_items
                    users_items.extend(times_range_items)

                # 取得非user的相同紀錄
                same_records_user_id    = func.get_same_record(user_unid,record_val)

                if same_records_user_id:
                    times_range_items   = {}
                    for other_user_id in same_records_user_id:
                        # 取得某位User瀏覽物件的資料
                        times_range_items   = func.get_times_range_items(other_user_id['user_id'],record_val)

                        if times_range_items:
                            others_user_items_dict.append(times_range_items)

                #將所有User都加起來(有興趣的物件)
                users_items2 = [user_items_dict] + others_user_items_dict

                # 全部可能喜歡的物件
                unique_items2 = sorted(list({ like_item
                                    for user_items in users_items2
                                    for like_item in user_items }))

                others_user_items_dict2 = sorted(list({ like_item
                                    for user_items in others_user_items_dict
                                    for like_item in user_items }))

                def make_user_interest_vector(user_interests):
                    return [1 if interest in user_interests else 0
                            for interest in unique_items2]
                user_interest_matrix = list(map(make_user_interest_vector, users_items2))

                user_similarities = [[func.cosine_similarity(interest_vector_i, interest_vector_j)
                      for interest_vector_j in user_interest_matrix]
                     for interest_vector_i in user_interest_matrix]

                # 推薦相似者喜歡的物件給他
                all_items     = func.user_based_suggestions(0, user_similarities,users_items2)
                recommand_items.extend(all_items)

# 檢查是否有已經close的物件，若有則取相似的物件替換
if recommand_items:
    recommand_items     = func.check_close(user_unid,recommand_items)

# 隨機取5個物件出來
if len(recommand_items) > 0 and len(recommand_items) < setting.random_num:
    print(recommand_items)
elif len(recommand_items) > 0:
    print(random.sample(recommand_items, setting.random_num))
else:
    print(users_items)