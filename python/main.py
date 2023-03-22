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
#user_unid = 'c24a6071c37e00d88b7ee7bbcd1a8724d'

func = FUNC_CLASS(user_unid)

users_items = []
recommand_items = []
unique_items = []

user_num = nolike_num = content_num = hot_num = new_num = search_num = 0

# 取得推薦權重
get_weight  = func.get_weight()
start_num = 6
for x in get_weight:
    if x[0] == 'user':
        user_num    = start_num
    elif x[0] == 'nolike':
        nolike_num  = start_num
    elif x[0] == 'content':
        content_num = start_num
    elif x[0] == 'hot':
        hot_num     = start_num
    elif x[0] == 'new':
        new_num     = start_num
    elif x[0] == 'search':
        search_num  = start_num
    start_num -= 1
#print(user_num,nolike_num,content_num,hot_num,new_num,search_num)
# 取得A的搜尋紀錄
record_data = func.get_this_user_search()
#print('record_data',record_data)
if len(record_data['often_record']) > 1:
    user_arr = []
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
                #print('A_itmes',times_range_items)
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

                        ret = list(set(user_items_dict).intersection(set(times_range_items)))
                        if times_range_items and len(ret) > 0:
                            others_user_items_dict.append(times_range_items)
                #print('others_user_items',others_user_items_dict)

                others_user_items_dict2 = sorted(list({ like_item
                                    for user_items in others_user_items_dict
                                    for like_item in user_items }))
                #print(record_val,'others_user_items_dict',others_user_items_dict)
                #print(record_val,'others_user_items_dict2',others_user_items_dict2)

                #如果毫無交集就跳過
                ret = list(set(user_items_dict).intersection(set(others_user_items_dict2)))

                if len(ret) == 0:
                    continue
                else:
                    others_user_items_dict2 = []
                    #檢查是否user的是否有在others
                    for user_items in others_user_items_dict:
                        ret = set(user_items_dict).intersection(set(user_items))
                        # 如果低於或是等於就不列入
                        if len(ret) > 0 and \
                            len(user_items) > len(ret):
                            others_user_items_dict2.append(user_items)

                #將所有User都加起來(有興趣的物件)
                users_items2 = [user_items_dict] + others_user_items_dict2
                #users_items2 = [user_items_dict] + [user_items]
                #print('users_items2',users_items2)
                # 全部可能喜歡的物件
                unique_items2 = sorted(list({ like_item
                                    for user_items in users_items2
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
                user_arr.extend(all_items)

    user_arr = random.sample(user_arr, (len(user_arr) if len(user_arr) < user_num else user_num))
    recommand_items.extend(user_arr)
    #print('User',user_arr)
# 如果筆數等於1，則推薦(該搜尋條件)熱門的
"""
elif len(record_data['often_record']) == 1:
    hot_house  = func.get_hot_house(record_data['last_record'][0])
    if len(hot_house) == 0:
        hot_house   = func.get_hot_house(record_data['last_record'][0],1)
    users_items = [(val['id']) for key, val in enumerate(hot_house)]

# 如果筆數等於0，則推薦(User所在區域)熱門的
else:
    hot_house   = func.get_hot_house([],2,user_unid)
    users_items = [(val['id']) for key, val in enumerate(hot_house)]
"""
####### 取得A(不喜愛)的物件，找到相同記錄、相同在意項目的人 #######
nolike_arr =[]
times_range_items_not = func.get_this_user_no_search()
nolike_arr.extend(times_range_items_not)
# 取得A曾經搜尋過的條件
user_all_record = func.get_user_all_record()
if len(user_all_record[0]) > 0:
    nolike_arr = func.get_user_all_record_items(user_all_record,nolike_arr)
    nolike_arr = random.sample(nolike_arr, (len(nolike_arr) if len(nolike_arr) < nolike_num else nolike_num))
    recommand_items.extend(nolike_arr)
#print('Nolike',nolike_arr)

####### 取得A(喜愛)的物件，找到相似內容的房子 #######
content_arr =[]
times_range_items_not = func.get_this_user_content(users_items)
content_arr.extend(times_range_items_not)
content_arr = random.sample(content_arr, (len(content_arr) if len(content_arr) < content_num else content_num))
recommand_items.extend(content_arr)
#print('content',content_arr)

####### 取得地區熱門 #######
bad_houses = ' AND `id` NOT IN ('+func.bad_houses+') ' if func.bad_houses != '' else ''
area_hot_arr    = func.get_user_all_record_items([[setting.default_area],[],[],[],[]],[],bad_houses+' ORDER BY `view_num` DESC LIMIT '+str(hot_num))
#print('area_hot_arr',area_hot_arr)
recommand_items.extend(area_hot_arr)
#print('area_hot',area_hot_arr)
####### 取得搜尋條件熱門 #######
search_hot_record = func.get_user_all_record(1);
if len(search_hot_record) == 0:
    search_hot_record   = [[setting.default_area],[],[],[],[]]
search_hot_arr    = func.get_user_all_record_items(search_hot_record,[],bad_houses+' ORDER BY `view_num` DESC LIMIT '+str(search_num))
recommand_items.extend(search_hot_arr)
#print('search_hot_arr',search_hot_arr)

####### 取得搜尋條件最新 #######
new_hot_record = func.get_user_all_record(1);
if len(new_hot_record) == 0:
    new_hot_record   = [[setting.default_area],[],[],[],[]]
new_hot_arr = func.get_user_all_record_items(new_hot_record,[],bad_houses+' ORDER BY `add_time` DESC, `view_num` DESC LIMIT '+str(new_num))
recommand_items.extend(new_hot_arr)
#print('new_hot_arr',new_hot_arr)

# 檢查是否有已經close的物件，若有則刪除
recommand_items = list(set(recommand_items))
if recommand_items:
    recommand_items     = func.check_close(recommand_items)

# 當推薦物件少於5筆時，加入User所在區域熱門的物件
"""
if len(recommand_items) < setting.less_how_num:
    recommand_items.extend(users_items)

    if len(recommand_items) < setting.less_how_num:
        if len(record_data['last_record']) == 0:
            hot_house   = func.get_hot_house([],2,user_unid)
        else:
            hot_house   = func.get_hot_house(record_data['last_record'][0],0,'',recommand_items)

        hot_house_arr = []
        for key, val in enumerate(hot_house):
            hot_house_arr.append(val['id'])
        recommand_items.extend(hot_house_arr)
        recommand_items = list(set(recommand_items))
"""
#print('recommand_items',recommand_items)
# 隨機取5個物件出來
if len(recommand_items) > 0 and len(recommand_items) < setting.random_num:
    print(random.sample(recommand_items, len(recommand_items)))
elif len(recommand_items) > 0:
    print(random.sample(recommand_items, setting.random_num))
else:
    print(users_items)