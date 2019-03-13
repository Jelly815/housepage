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

user_items_dict = []
others_user_items_dict = []
times_range_items = []

# 取得user的搜尋紀錄
record_data = func.get_this_user_search(user_unid)

for key,record in record_data.items():
    if record:  
        for record_val in record:
            # 取得usre(喜愛)的物件(瀏覽時間大於5秒,瀏覽次數大於1)
            times_range_items = func.get_times_range_items(user_unid,record_val)
            
            # 取得usre項目
            #times_range_items = func.get_times_range_items(user_unid,record_val)
            
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
users_interests = user_items_dict + others_user_items_dict
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

    # 第一個即是user
    print(most_similar_interests_to(0))


