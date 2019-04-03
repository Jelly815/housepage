# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:23:18 2019

@author: Jelly
"""
from function import FUNC_CLASS
import sys
import os
import setting
#user_unid = sys.argv[1]
#user_unid = 'm199cdc39ee6e65811960a187ccf1fcb9'
user_unid = '7f16a3540e74b904ed3ee626c79af314'
func = FUNC_CLASS()

user_items_dict = []
others_user_items_dict = []
times_range_items = []
re_val = []
# 取得A的搜尋紀錄
record_data = func.get_this_user_search(user_unid)

# 取得A(不喜愛)的物件
times_range_items_not = func.get_this_user_no_search(user_unid)
#print(times_range_items_not)
if len(record_data['often_record']) > 1:
    for key,record in record_data.items():
        if record:
            for record_val in record:
                # 取得A(喜愛)的物件(瀏覽時間大於5秒,瀏覽次數大於1or有加入最愛)
                times_range_items = func.get_times_range_items(user_unid,record_val)

                if times_range_items:
                    user_items_dict.append(times_range_items)

                # 取得非user的相同紀錄
                same_records_user_id = func.get_same_record(user_unid,record_val)

                if same_records_user_id:
                    times_range_items = {}
                    for other_user_id in same_records_user_id:
                        # 取得某位User瀏覽物件的資料
                        times_range_items = func.get_times_range_items(other_user_id['unid'],record_val)

                        if times_range_items:
                            others_user_items_dict.append(times_range_items)
    #將所有User都加起來
    users_interests = user_items_dict + others_user_items_dict

    print('user_items_dict',user_items_dict)
    print('others_user_items_dict',others_user_items_dict)
    print('times_range_items_not',times_range_items_not)
    if len(users_interests) == 0:
        #找到相同記錄、相同在意項目的人
        print(times_range_items_not)
        #找到其他User後，取出不喜歡的項目
        #尋找這些不喜歡的項目內，是否有相似的使用者
        #取得相似的使用者，獲得該使用者喜歡的物件
        #如果users_interests的項目不足5項該怎麼處理


# 如果筆數等於1，則推薦(該搜尋條件)熱門的
elif len(record_data['often_record']) == 1:
    hot_house  = func.get_hot_house(record_data['often_record'][0])
    if len(hot_house) == 0:
        hot_house   = func.get_hot_house(record_data['often_record'][0],1)
    unique_items = [(val['id']) for key, val in enumerate(hot_house)]

# 如果筆數等於0，則推薦(User所在區域)熱門的
else:
    hot_house   = func.get_hot_house([],2,user_unid)
    unique_items = [(val['id']) for key, val in enumerate(hot_house)]

def most_similar_interests_to(interest_id):
    similarities = interest_similarities[interest_id]

    pairs = [(unique_items[other_interest_id], similarity)
             for other_interest_id, similarity in enumerate(similarities)
             if interest_id != other_interest_id and similarity > 0]

    return sorted(pairs,
                  key=lambda pair: pair[1],
                  reverse=True)

# 對於該物件是否有興趣，是:1,否:0
def make_user_items_matrix(others_user_items_dict):
    return [1 if interest in others_user_items_dict else 0
            for interest in unique_items]

# 全部可能喜歡的物件
unique_items = sorted(list({ interest
                         for user_interests in users_interests
                         for interest in user_interests }))
if unique_items:
    # 使用者>興趣，是:1,否:0
    user_interest_matrix = list(map(make_user_items_matrix, users_interests))

    # 興趣>使用者，是:1,否:0
    interest_user_matrix = [[user_interest_vector[j]
                         for user_interest_vector in user_interest_matrix]
                        for j, _ in enumerate(unique_items)]
    # 使用餘弦相似度
    interest_similarities = [[func.cosine_similarity(user_vector_i, user_vector_j)
                      for user_vector_j in interest_user_matrix]
                     for user_vector_i in interest_user_matrix]

    # 第一個即是A
    print(most_similar_interests_to(0))
    #most_similar_interests_to(0)


