# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 23:57:35 2018

@author: Jelly
"""

import math, random
import pandas as pd
import numpy as np
from collections import defaultdict, Counter

users_interests = [
    ["01", "02", "03"],
    ["01", "02", "04"],
    ["01", "02", "05"],
    ["01", "05", "06"]
]

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


unique_interests = sorted(list({ interest
                                 for user_interests in users_interests
                                 for interest in user_interests }))
    
def make_user_interest_vector(user_interests):
    """given a list of interests, produce a vector whose i-th element is 1
    if unique_interests[i] is in the list, 0 otherwise"""
    return [1 if interest in user_interests else 0
            for interest in unique_interests]

def cosine_similarity(v, w):
    return dot(v, w) / math.sqrt(dot(v, v) * dot(w, w))

def most_similar_interests_to(interest_id):
    similarities = interest_similarities[interest_id]

    pairs = [(unique_interests[other_interest_id], similarity)
             for other_interest_id, similarity in enumerate(similarities)
             if interest_id != other_interest_id and similarity > 0]
    return sorted(pairs,
                  key=lambda pair: pair[1],
                  reverse=True)

def item_based_suggestions(user_id, include_current_interests=False):
    suggestions = defaultdict(float)
    user_interest_vector = user_interest_matrix[user_id]
    for interest_id, is_interested in enumerate(user_interest_vector):
        if is_interested == 1:
            similar_interests = most_similar_interests_to(interest_id)
            for interest, similarity in similar_interests:
                suggestions[interest] += similarity

    suggestions = sorted(suggestions.items(),
                         key=lambda pair: pair[1],
                         reverse=True)

    if include_current_interests:
        return suggestions
    else:
        return [(suggestion, weight)
                for suggestion, weight in suggestions
                if suggestion not in users_interests[user_id]]

user_interest_matrix = list(map(make_user_interest_vector, users_interests))
user_similarities = [[cosine_similarity(interest_vector_i, interest_vector_j)
                      for interest_vector_j in user_interest_matrix]
                     for interest_vector_i in user_interest_matrix]
print('user_interest_matrix',user_interest_matrix)
def most_similar_users_to(user_id):
    pairs = [(other_user_id, similarity)                      # find other
             for other_user_id, similarity in                 # users with
                enumerate(user_similarities[user_id])         # nonzero
             if user_id != other_user_id and similarity > 0]  # similarity

    return sorted(pairs,                                      # sort them
                  key=lambda pair: pair[1],                   # most similar
                  reverse=True)                               # first

def user_based_suggestions(user_id, include_current_interests=False):
    # sum up the similarities
    suggestions = defaultdict(float)
    for other_user_id, similarity in most_similar_users_to(user_id):
        for interest in users_interests[other_user_id]:
            suggestions[interest] += similarity

    # convert them to a sorted list
    suggestions = sorted(suggestions.items(),
                         key=lambda pair: pair[1],
                         reverse=True)
    print(suggestions)
    # and (maybe) exclude already-interests
    if include_current_interests:
        return suggestions
    else:
        return [(suggestion, weight)
                for suggestion, weight in suggestions
                if suggestion not in users_interests[user_id]]


#print(unique_interests)
# user_interest_matrix[0]:使用者對36項是否有興趣，是:1,否:0


# interest_user_matrix[0]:15個使用者，對於該項是否有興趣，是:1,否:0
interest_user_matrix = [[user_interest_vector[j]
                         for user_interest_vector in user_interest_matrix]
                        for j, _ in enumerate(unique_interests)]

# 使用餘弦相似度
interest_similarities = [[cosine_similarity(user_vector_i, user_vector_j)
                          for user_vector_j in interest_user_matrix]
                         for user_vector_i in interest_user_matrix]

#print(most_similar_interests_to(0))
print(user_based_suggestions(0))


del_index       = None
#data = {'time':[30,30,60,60,100,150,300,300,500,700]}
#data = {'time':[30,30,60,60,100,150,300,300,500]}
data = {'time':[30,30,60,60,100,150,300,300]}
df = pd.DataFrame(data)
df_NaN = df[df.isnull().any(axis=1)].index.values

# 刪除 NaN 值
df.dropna(inplace=True)

# abs:絕對值;  abs(X - 平均值)；mean:取均值
df['x-Mean']    = abs(df['time'] - df['time'].mean())
# std:標準差，有 95% 信心估計母群體平均數，在樣本平均數 ± 1.96 * (母群體標準差 / 樣本數 n 的平方根) 的範圍內。
df['1.96*std']  = 1.96*df['time'].std()
df['Outlier']   = abs(df['time'] - df['time'].mean()) > 1.96*df['time'].std()
print(df['Outlier'])
# 刪除為True的資料
for x in range(len(df)):
    this_bool = df.iloc[x]['Outlier']
    del_index = x if this_bool else None

print([df_NaN,del_index])

user = [ 21, 17, 17, 20, 19, 17, 20, 20, 22, 20 ]
other = [25.5,28,24,23.4,25]

print('user_std',np.std(user))
print('user_mean',np.mean(user))

median = [30,60,90,100,150,300]
new_data    = set(median)
p_index     = int(0.5 * len(new_data))
print('median',sorted(new_data)[p_index])
