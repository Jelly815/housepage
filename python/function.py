# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 00:58:08 2019

@author: Jelly
"""

from db_connect import DB_CONN
import setting
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from collections import defaultdict
import json

class FUNC_CLASS(DB_CONN):

    def __init__(self):
        super().__init__()
        # 項目總數
        self.items_len   = len(setting.similar_list + setting.range_list)

    # 取得最早的上線時間
    def get_user_login_time(self):
        login_day = 0

        login_time_sql      = """
            SELECT  `last_time`
            FROM    `ex_record`
            ORDER BY `last_time`
            LIMIT 1
            """

        try:
            self.execute(login_time_sql)
            record_arr = self.fetchall()

            if record_arr:
                login_time  = str(record_arr[0]['login_time'])

                today       = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                start       = datetime.datetime.strptime(login_time, '%Y-%m-%d %H:%M:%S')
                end         = datetime.datetime.strptime(today, '%Y-%m-%d %H:%M:%S')
                login_day   = (end - start).days
        except:
            login_day = 0

        return login_day

    # 取得user的搜尋紀錄(喜歡)
    def get_this_user_search(self,user_id):
        user_record = {}
        user_record['last_record']  = []
        user_record['often_record'] = []

        if user_id != '':
            user_sql    = """
                SELECT  `area`,`price`,`ping`,`style`,`type`
                FROM    `ex_record`
                WHERE   `user_id` = %s AND
                        `last_time` BETWEEN (NOW() - INTERVAL %s DAY) AND NOW()
                """

            try:
                # 取得user [最後]搜尋的條件
                self.execute(user_sql+" ORDER BY `last_time` DESC,times DESC LIMIT 1",\
                    [user_id,setting.search_house_days])
                user_last_arr = self.fetchall()

                if(user_last_arr is not None):
                    for x, last in enumerate(user_last_arr):
                        user_record['last_record'].append([last['area'],last['price'],last['ping'],last['style'],last['type']])

                # 取得user [經常]搜尋的條件
                self.execute(user_sql+" GROUP by  `area`,`price`,`ping`,`style`,`type` \
                    ORDER BY `times` DESC,`last_time` DESC,`price`,`ping` DESC LIMIT 3",\
                    [user_id,setting.search_house_days])
                user_often_arr = self.fetchall()
                #print('user_often_arr',user_often_arr)
                if user_often_arr is not None:
                    for x, often in enumerate(user_often_arr):
                        user_record['often_record'].append([often['area'],often['price'],often['ping'],often['style'],often['type']])

            except:
                user_record = {}
                user_record['last_record']  = []
                user_record['often_record'] = []

        return user_record

    # 取得user的搜尋紀錄(不喜歡)
    def get_this_user_no_search(self,user_id):
        user_record = {}
        user_range  = {}
        user_recommend  = []
        out_items   = ['around','road','description']

        if user_id != '':
            # 取得useritems_str 半年內的搜尋紀錄
            user_today_sql = """
                SELECT  record.`id`,record.`area`,record.`price`,
                        record.`ping`,record.`style`,record.`type`,items.`main_id`
                FROM    `ex_record` record,`ex_record_items` items
                WHERE   record.`id` = items.`record_id` AND
                        record.`user_id` = %s AND
                        record.`last_time` BETWEEN (NOW() - INTERVAL %s DAY) AND NOW() AND
                        items.`times` = 1 AND
                        items.`add_favorite` = 0
                ORDER BY record.`last_time` DESC
                """

            try:
                self.execute(user_today_sql,[user_id,setting.search_house_days])
                user_today_arr  = self.fetchall()

                user_items_arr   = {
                        'area':[],'road':[],'room':[],
                        'ping':[],'parking':[],'age':[],
                        'floor':[],'type':[],'direction':[],
                        'fee':[],'builder':[],'unit':[],
                        'price':[],'description':[],'around':[],
                        'status':[],'community':[]
                }

                if len(user_today_arr) > 0:
                    for x, user_today in enumerate(user_today_arr):
                        record  = [user_today['area'],user_today['price'],user_today['ping'],user_today['style'],user_today['type']]

                        users_all = []
                        # 取得非user有相同記錄的人
                        users   = [val['user_id'] for y,val in enumerate(self.get_same_record(user_id,record))]

                        if len(users) > 0:
                            users_all.extend(users)

                        user_today_sql = """
                            SELECT  `community`,`status`,`around`,`description`,`price`,`unit`,`builder`,`fee`,
                                    `direction`,`type`,`floor`,`age`,`parking`,`ping`,`room`,`road`,`area`
                            FROM    `ex_main`
                            WHERE   `id` = %s
                            """

                        self.execute(user_today_sql,[user_today['main_id']])

                        this_user_mains = self.fetchall()
                        #print('this_user_mains',this_user_mains)
                        for x,val in enumerate(this_user_mains):
                            new_row = list(val)
                            for i in new_row:
                                if i == 'description':  #主建物坪數
                                    #user_items_arr[i].append(self.get_description(val[i]))
                                    user_items_arr[i].append("")
                                elif val[i] is not None:
                                    user_items_arr[i].append(val[i])

                    #找到其他User後，取出不喜歡的項目
                    users_all = list(set(users_all))
                    print('users_all',users_all)
                    for unid in users_all:
                        user_today_sql = """
                            SELECT  `items`
                            FROM    `ex_record_items_obj`
                            WHERE   `user_id` = %s AND `is_like` = 2
                            """
                        self.execute(user_today_sql,[unid])
                        other_user_nolike_json= self.fetchall()
                        print('other_user_nolike_json',other_user_nolike_json)
                        #user_record[unid] = json.loads(other_user_nolike_json[0]['items'])

                    #print('user_record',user_record)
                    if len(user_items_arr['area']) > 0 and len(user_record) > 0:
                        for user_id,record_items in  user_record.items():
                            if len(record_items['area']) == 0:
                                continue
                            user_to_others = []

                            for key,values in record_items.items():
                                if key in out_items:
                                    continue
                                # 比對是否有一樣的
                                elif key in setting.similar_list and len(values) > 0:
                                    #print('values',values)
                                    #print('user_items_arr',user_items_arr[key])
                                    intersection = list(set(map(lambda x: str(x), user_items_arr[key])) & set(values))
                                    #print('intersection',intersection)

                                    user_items_count = 0
                                    for x in user_items_arr[key]:
                                        if str(x) in intersection:
                                            user_items_count = user_items_count + 1
                                    user_percent = round((user_items_count / len(user_items_arr[key])),3) if len(user_items_arr[key]) != 0 else 0

                                    others_items_count = 0
                                    for x in values:
                                        if x in intersection:
                                            others_items_count = others_items_count + 1
                                    others_percent = round((others_items_count / len(values)),3) if len(values) != 0 else 0
                                    #print('user_percent',user_percent)
                                    #print('others_percent',others_percent)
                                    # 兩者相似的大於一半才算
                                    user_to_others.append(1 if (user_percent >= setting.similar_percent and others_percent >= setting.similar_percent) else 0)

                                # 比對是否在範圍內
                                elif key in setting.range_list and len(values) > 0:
                                    values      = list(map(lambda x: float(x), values))
                                    user_items_arr[key]  = list(map(lambda x: float(x), user_items_arr[key]))

                                    # 計算平均值(this user)
                                    mean_num_user   = np.mean(user_items_arr[key])
                                    # 計算平均值(other)
                                    mean_num_other  = np.mean(values)

                                    # 價格
                                    if key == 'price':
                                        if mean_num_user <= 300:
                                            user_val = 1
                                        elif 300 < mean_num_user <= 600:
                                            user_val = 2
                                        elif 600 < mean_num_user <= 1000:
                                            user_val = 3
                                        elif 1000 < mean_num_user <= 1500:
                                            user_val = 4
                                        elif 1500 < mean_num_user <= 2000:
                                            user_val = 5
                                        elif mean_num_user > 2000:
                                            user_val = 6

                                        if mean_num_other <= 300:
                                            other_val = 1
                                        elif 300 < mean_num_other <= 600:
                                            other_val = 2
                                        elif 600 < mean_num_other <= 1000:
                                            other_val = 3
                                        elif 1000 < mean_num_other <= 1500:
                                            other_val = 4
                                        elif 1500 < mean_num_other <= 2000:
                                            other_val = 5
                                        elif mean_num_other > 2000:
                                            other_val = 6

                                        # 兩者區間範圍相同就算
                                        user_to_others.append(1 if user_val == other_val else 0)
                                    elif key == 'ping':
                                        #坪數
                                        if mean_num_user <= 20:
                                            user_val = 1
                                        elif 20 < mean_num_user <= 30:
                                            user_val = 2
                                        elif 30 < mean_num_user <= 40:
                                            user_val = 3
                                        elif 40 < mean_num_user <= 50:
                                            user_val = 4
                                        elif mean_num_user > 50:
                                            user_val = 5

                                        if mean_num_other <= 20:
                                            other_val = 1
                                        elif 20 < mean_num_other <= 30:
                                            other_val = 2
                                        elif 30 < mean_num_other <= 40:
                                            other_val = 3
                                        elif 40 < mean_num_other <= 50:
                                            other_val = 4
                                        elif mean_num_other > 50:
                                            other_val = 5

                                        # 兩者區間範圍相同就算
                                        user_to_others.append(1 if user_val == other_val else 0)
                                    else:
                                        # 計算標準差
                                        std_num     = np.std(values)
                                        # 計算範圍值
                                        star_num    = mean_num_other - std_num
                                        end_num     = mean_num_other + std_num

                                        # 範圍內的大於一半才算
                                        intersection= [1 if x >= star_num and x <= end_num else 0
                                                       for x in user_items_arr[key]]

                                        percent = round((sum(intersection) / len(user_items_arr[key])),3) if len(user_items_arr[key]) != 0 else 0
                                        user_to_others.append(1 if len(intersection) > 0 and percent >= setting.similar_percent else 0)
                                else:
                                    user_to_others.append(0)

                                #print('user_to_others',user_to_others)
                            user_range[user_id] = round((sum(user_to_others) / self.items_len),3)
                            #print('user_range',user_range)
                            # 排除相似度小於0.5的User
                            if float(user_range[user_id]) < setting.similar_percent:
                                del user_range[user_id]

                # 找到的User，依照相似度高至低排序
                user_range  = sorted(user_range.items(), key=lambda d: d[1], reverse=True)
                #print('user_range',user_range)
                # 依照搜尋紀錄、相似者，找到喜愛的物件
                for user in user_range:
                    # 找到該User喜愛物件的搜尋條件id
                    user_record_sql = """
                        SELECT  `items`
                        FROM    `ex_record_items_obj`
                        WHERE   `user_id`   = %s AND
                                `is_like` = 2
                        """
                    try:
                        self.execute(user_record_sql,[user[0]])
                        user_record_arr     = self.fetchall()
                        #print('user_record_arr',user_record_arr)
                        user_recommend = [int(x) for x in user_record_arr[0]['items'].split(',')]
                    except:
                        user_record_arr     = {}
            except:
                user_recommend = []

        return list(set(user_recommend))

    # 依內容比對
    def get_this_user_content(self,user_id):
        user_record = {}
        user_range  = {}
        user_recommend  = []
        out_items   = ['around','road','description']

        if user_id != '':
            # 取得useritems_str 半年內的搜尋紀錄
            user_today_sql = """
                SELECT  record.`id`,record.`area`,record.`price`,
                        record.`ping`,record.`style`,record.`type`,items.`main_id`
                FROM    `ex_record` record,`ex_record_items` items
                WHERE   record.`id` = items.`record_id` AND
                        record.`user_id` = %s AND
                        record.`last_time` BETWEEN (NOW() - INTERVAL %s DAY) AND NOW() AND
                        items.`times` = 1 AND
                        items.`add_favorite` = 0
                ORDER BY record.`last_time` DESC
                """

            try:
                self.execute(user_today_sql,[user_id,setting.search_house_days])
                user_today_arr  = self.fetchall()

                user_items_arr   = {
                        'area':[],'road':[],'room':[],
                        'ping':[],'parking':[],'age':[],
                        'floor':[],'type':[],'direction':[],
                        'fee':[],'builder':[],'unit':[],
                        'price':[],'description':[],'around':[],
                        'status':[],'community':[]
                }

                if len(user_today_arr) > 0:
                    for x, user_today in enumerate(user_today_arr):
                        record  = [user_today['area'],user_today['price'],user_today['ping'],user_today['style'],user_today['type']]
                        print(user_today['id'])
                        users_all = []
                        # 取得非user有相同記錄的人
                        users   = [val['user_id'] for y,val in enumerate(self.get_same_record(user_id,record))]

                        if len(users) > 0:
                            users_all.extend(users)
                        #print('users_all',users_all)

                        user_today_sql = """
                            SELECT  `community`,`status`,`around`,`description`,`price`,`unit`,`builder`,`fee`,
                                    `direction`,`type`,`floor`,`age`,`parking`,`ping`,`room`,`road`,`area`
                            FROM    `ex_main`
                            WHERE   `id` = %s
                            """

                        self.execute(user_today_sql,[user_today['main_id']])

                        this_user_mains = self.fetchall()
                        print('this_user_mains',this_user_mains)
                        for x,val in enumerate(this_user_mains):
                            new_row = list(val)
                            for i in new_row:
                                if i == 'description':  #主建物坪數
                                    #user_items_arr[i].append(self.get_description(val[i]))
                                    user_items_arr[i].append("")
                                elif val[i] is not None:
                                    user_items_arr[i].append(val[i])

                    #找到其他User後，取出不喜歡的項目
                    users_all = list(set(users_all))
                    for unid in users_all:
                        user_today_sql = """
                            SELECT  `items`
                            FROM    `ex_record_items_obj`
                            WHERE   `user_id` = %s AND `is_like` = 0
                            """
                        self.execute(user_today_sql,[unid])
                        other_user_nolike_json= self.fetchall()
                        user_record[unid] = json.loads(other_user_nolike_json[0]['items'])
                    #print('user_items_arr',user_items_arr)
                    #print('user_record',user_record)
                    if len(user_items_arr['area']) > 0 and len(user_record) > 0:
                        for user_id,record_items in  user_record.items():
                            if len(record_items['area']) == 0:
                                continue
                            user_to_others = []

                            for key,values in record_items.items():
                                if key in out_items:
                                    continue
                                # 比對是否有一樣的
                                elif key in setting.similar_list and len(values) > 0:
                                    #print('values',values)
                                    #print('user_items_arr',user_items_arr[key])
                                    intersection = list(set(map(lambda x: str(x), user_items_arr[key])) & set(values))
                                    #print('intersection',intersection)

                                    user_items_count = 0
                                    for x in user_items_arr[key]:
                                        if str(x) in intersection:
                                            user_items_count = user_items_count + 1
                                    user_percent = round((user_items_count / len(user_items_arr[key])),3) if len(user_items_arr[key]) != 0 else 0

                                    others_items_count = 0
                                    for x in values:
                                        if x in intersection:
                                            others_items_count = others_items_count + 1
                                    others_percent = round((others_items_count / len(values)),3) if len(values) != 0 else 0
                                    #print('user_percent',user_percent)
                                    #print('others_percent',others_percent)
                                    # 兩者相似的大於一半才算
                                    user_to_others.append(1 if (user_percent >= setting.similar_percent and others_percent >= setting.similar_percent) else 0)

                                # 比對是否在範圍內
                                elif key in setting.range_list and len(values) > 0:
                                    values      = list(map(lambda x: float(x), values))
                                    user_items_arr[key]  = list(map(lambda x: float(x), user_items_arr[key]))

                                    # 計算平均值(this user)
                                    mean_num_user   = np.mean(user_items_arr[key])
                                    # 計算平均值(other)
                                    mean_num_other  = np.mean(values)

                                    # 價格
                                    if key == 'price':
                                        if mean_num_user <= 300:
                                            user_val = 1
                                        elif 300 < mean_num_user <= 600:
                                            user_val = 2
                                        elif 600 < mean_num_user <= 1000:
                                            user_val = 3
                                        elif 1000 < mean_num_user <= 1500:
                                            user_val = 4
                                        elif 1500 < mean_num_user <= 2000:
                                            user_val = 5
                                        elif mean_num_user > 2000:
                                            user_val = 6

                                        if mean_num_other <= 300:
                                            other_val = 1
                                        elif 300 < mean_num_other <= 600:
                                            other_val = 2
                                        elif 600 < mean_num_other <= 1000:
                                            other_val = 3
                                        elif 1000 < mean_num_other <= 1500:
                                            other_val = 4
                                        elif 1500 < mean_num_other <= 2000:
                                            other_val = 5
                                        elif mean_num_other > 2000:
                                            other_val = 6

                                        # 兩者區間範圍相同就算
                                        user_to_others.append(1 if user_val == other_val else 0)
                                    elif key == 'ping':
                                        #坪數
                                        if mean_num_user <= 20:
                                            user_val = 1
                                        elif 20 < mean_num_user <= 30:
                                            user_val = 2
                                        elif 30 < mean_num_user <= 40:
                                            user_val = 3
                                        elif 40 < mean_num_user <= 50:
                                            user_val = 4
                                        elif mean_num_user > 50:
                                            user_val = 5

                                        if mean_num_other <= 20:
                                            other_val = 1
                                        elif 20 < mean_num_other <= 30:
                                            other_val = 2
                                        elif 30 < mean_num_other <= 40:
                                            other_val = 3
                                        elif 40 < mean_num_other <= 50:
                                            other_val = 4
                                        elif mean_num_other > 50:
                                            other_val = 5

                                        # 兩者區間範圍相同就算
                                        user_to_others.append(1 if user_val == other_val else 0)
                                    else:
                                        # 計算標準差
                                        std_num     = np.std(values)
                                        # 計算範圍值
                                        star_num    = mean_num_other - std_num
                                        end_num     = mean_num_other + std_num

                                        # 範圍內的大於一半才算
                                        intersection= [1 if x >= star_num and x <= end_num else 0
                                                       for x in user_items_arr[key]]

                                        percent = round((sum(intersection) / len(user_items_arr[key])),3) if len(user_items_arr[key]) != 0 else 0
                                        user_to_others.append(1 if len(intersection) > 0 and percent >= setting.similar_percent else 0)
                                else:
                                    user_to_others.append(0)

                                #print('user_to_others',user_to_others)
                            user_range[user_id] = round((sum(user_to_others) / self.items_len),3)
                            #print('user_range',user_range)
                            # 排除相似度小於0.5的User
                            if float(user_range[user_id]) < setting.similar_percent:
                                del user_range[user_id]

                # 找到的User，依照相似度高至低排序
                user_range  = sorted(user_range.items(), key=lambda d: d[1], reverse=True)
                #print('user_range',user_range)
                # 依照搜尋紀錄、相似者，找到喜愛的物件
                for user in user_range:
                    # 找到該User喜愛物件的搜尋條件id
                    user_record_sql = """
                        SELECT  `items`
                        FROM    `ex_record_items_obj`
                        WHERE   `user_id`   = %s AND
                                `is_like` = 2
                        """
                    try:
                        self.execute(user_record_sql,[user[0]])
                        user_record_arr     = self.fetchall()
                        #print('user_record_arr',user_record_arr)
                        user_recommend = [int(x) for x in user_record_arr[0]['items'].split(',')]
                    except:
                        user_record_arr     = {}
            except:
                user_recommend = []

        return list(set(user_recommend))

    # 取得非user有相同記錄的人
    def get_same_record(self,user_id,record,limit=1):
        record_arr = {}

        # 取得user record
        record_sql = """
            SELECT  `user_id`
            FROM    `ex_record`
            WHERE   `user_id` != %s AND
                    `area`    = %s AND
                    `price`   = %s AND
                    `ping`    = %s AND
                    `style`   = %s AND
                    `type`    = %s
            """

        record_vals = [
                user_id,
                record[0],record[1],record[2],
                record[3],record[4]
        ]

        try:
            if(record):
                self.execute(record_sql,record_vals)
                record_arr = self.fetchall()
            else:
                # 若setting.search_house_days設定的天數找不到資料，則往回推天數，直到找到資料
                limit += 1

                login_last_day = self.get_user_login_time()
                if login_last_day > setting.search_house_days:
                    limit_round = int(login_last_day / setting.search_house_days)

                    if limit <= limit_round:
                        self.get_same_record(user_id,record,limit)

        except:
            record_arr = {}

        return record_arr

    # 取得某位User瀏覽物件的資料
    def get_times_range_items(self,user_id,record):
        record_arr = {}
        is_favorite_items = []
        new_arr = {
                    'user_id':[],
                    'record_times':[],
                    'main_id':[],
                    'items_times':[],
                    'click_map':[],
                    'add_favorite':[],
                    'item_stay_time':[]
                }

        # 取得user record
        record_sql = """
            SELECT  `user_id`,`record_times`,`main_id`,`items_times`,`click_map`,
                    `add_favorite`,`item_stay_time`
            FROM    `ex_user_record_view`
            WHERE   `user_id` = %s AND
                    `area`    = %s AND
                    `price`   = %s AND
                    `ping`    = %s AND
                    `style`   = %s AND
                    `type`    = %s
            ORDER BY `item_stay_time`
            """

        record_vals = [
                user_id,record[0],
                record[1],record[2],record[3],
                record[4]]

        try:
            if record:
                #print(record_sql,record_vals)
                self.execute(record_sql,record_vals)
                record_arr = self.fetchall()

                if record_arr:
                    for _, record in enumerate(record_arr):
                        for key,val in record.items():
                            new_arr[key].append(val)

                # 如果User有加入最愛的習慣1;反之0
                is_like = 1 if sum(new_arr['add_favorite']) > 0 else 0

                user_time_range = 0
                if is_like == 0:
                    # 刪除[物件停留時間]離群值
                    is_outlier = True
                    outlier_index = self.get_outlier(new_arr,'item_stay_time')

                    while is_outlier:
                        if outlier_index[1] is not None:
                            del record_arr[outlier_index[1]]
                            for x in new_arr:
                                del new_arr[x][outlier_index[1]]
                            is_outlier = False
                        else:
                            is_outlier = False

                    is_favorite_items = []
                    if new_arr['item_stay_time']:
                        # 取得該User瀏覽區間
                        user_time_range = self.get_user_time_range(list(set(new_arr['item_stay_time'])))

                        # 某user喜歡物件的時間圓餅圖
                        #if new_arr['item_stay_time']:
                        #    self.plt_pie(new_arr)

                # 取得該範圍內，User的物件
                is_favorite_items = self.get_is_favorite(new_arr,['main_id','add_favorite','item_stay_time'],user_time_range,is_like)
        except:
            is_favorite_items = []

        return is_favorite_items

    # 取得分類最熱門的房子(no_data=0，有1筆記錄；no_data=1:有1筆記錄，但資料不足；no_data=:完全沒資料)
    def get_hot_house(self,record,no_data=0,user_id='',items=[]):
        hot_house_vals = []
        hot_house_sql  = """
                SELECT  `id`
                FROM    `ex_main`
                """

        if no_data == 1:
            hot_house_sql  += """
                WHERE   `area` = %s AND
                        `price`= %s AND
                        `is_closed` = 0
                ORDER BY `view_num` DESC,`update_time` DESC
                LIMIT 5
                """
            hot_house_vals  = [record[0],record[3]]
        elif no_data == 2:
            user_area_sql   = "SELECT `area_id` FROM `ex_user` WHERE unid = %s"
            self.execute(user_area_sql,[user_id])
            user_area       = self.fetchall()

            hot_house_vals = ''
            if user_area:
                hot_house_vals  = [user_area[0]['area_id']]
                hot_house_sql  += " WHERE   `area` = %s AND "
            else:
                hot_house_vals = [setting.default_area]
                if hot_house_vals:
                    hot_house_sql  += " WHERE   `area` = %s AND "
                else:
                    hot_house_vals = []
                    for num in range(276,318) :
                        hot_house_vals.append(num)

                    hot_house_sql  += " WHERE   `area` IN ("+ ','.join((str(num) for num in hot_house_vals)) +") AND "
                    hot_house_vals = []

            hot_house_sql  += """
                        `is_closed` = 0
                ORDER BY `view_num` DESC,`update_time` DESC
                LIMIT 5
                """
        else:
            hot_house_sql  += " WHERE "
            if len(items) > 0:
                hot_house_sql  += " `id` NOT IN ("+','.join(str(e) for e in items)+") AND "

            # 價格
            if record[1] == 300:
                hot_house_sql  += " `price`<= 300 AND "
            elif record[1] == 600:
                hot_house_sql  += " `price` BETWEEN 300 AND 600 AND "
            elif record[1] == 1000:
                hot_house_sql  += " `price` BETWEEN 600 AND 1000 AND "
            elif record[1] == 1500:
                hot_house_sql  += " `price` BETWEEN 1000 AND 1500 AND "
            elif record[1] == 2000:
                hot_house_sql  += " `price` BETWEEN 1500 AND 2000 AND "
            elif record[1] == 2001:
                hot_house_sql  += " `price` >= 2000 AND "
            #坪數
            if record[2] == 20:
                hot_house_sql  += " `ping`<= 20 AND "
            elif record[2] == 30:
                hot_house_sql  += " `ping` BETWEEN 20 AND 30 AND "
            elif record[2] == 40:
                hot_house_sql  += " `ping` BETWEEN 30 AND 40 AND "
            elif record[2] == 50:
                hot_house_sql  += " `ping` BETWEEN 40 AND 50 AND "
            elif record[2] == 51:
                hot_house_sql  += " `ping` >= 51 AND "

            hot_house_sql  += """
                        `area` = %s AND
                        `room`= %s AND
                        `type` = %s AND
                        `is_closed` = 0
                ORDER BY `view_num` DESC,`update_time` DESC
                LIMIT 5
                """
            hot_house_vals = [record[0],record[3],record[4]]
        try:
            #print(hot_house_sql,hot_house_vals)
            if hot_house_vals:
                self.execute(hot_house_sql,hot_house_vals)
            else:
                self.execute(hot_house_sql)
            hot_house      = self.fetchall()

        except:
            hot_house = []

        return hot_house

    # 取得分位數
    def quantile(self,data,percent):
        # 排除重複
        new_data    = set(data)
        p_index     = int(percent * len(new_data))
        return sorted(new_data)[p_index]

    # 某user喜歡物件的時間圓餅圖
    def plt_pie(self,data):
        explode = []
        df      = pd.DataFrame(data)

        labels  = df['main_id']
        sizes   = df['item_stay_time']

        median_num = round(len(data['item_stay_time']))

        for zero,_ in enumerate(data['item_stay_time']):
            explode.append(0.1 if (zero + 1) == median_num else 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True)
        ax1.axis('equal')
        plt.show()

    # 取得離群值的資料index
    def get_outlier(self,data,field):
        del_index       = None
        df = pd.DataFrame(data, columns=[field])
        df_NaN = df[df.isnull().any(axis=1)].index.values

        # 刪除 NaN 值
        df.dropna(inplace=True)

        if not df.empty:
            # abs:絕對值;  abs(X - 平均值)；mean:取均值
            x_mean          = abs(df[field] - df[field].mean())
            # std:標準差，有 95% 信心估計母群體平均數，在樣本平均數 ± 1.96 * (母群體標準差 / 樣本數 n 的平方根) 的範圍內。
            std_196         = 1.96*df[field].std()
            df['outlier']   = x_mean > std_196

            # 刪除為True的資料
            for x in range(len(df)):
                this_bool = df.iloc[x]['outlier']
                del_index = x if this_bool else None

        return [df_NaN,del_index]

    # 取得該User瀏覽時間的中位數
    def get_user_time_range(self,data):
        time_range = self.quantile(data,0.5) if data else 0

        return time_range

    # 取得該時間範圍，User有加入最愛的物件
    def get_is_favorite(self,data,columns_list,time_range,is_like):
        items_arr   = []
        df = pd.DataFrame(data, columns=columns_list)
        df = df[df['item_stay_time'] >= time_range]

        # 如果有加入最愛，則把該物件加入list
        if is_like == 1:
            df_favorite = df[df.add_favorite == 1]

            if not df_favorite.empty:
                for x in df_favorite.index:
                    items_arr.append(df['main_id'][x])
            else:
                items_arr = df.main_id
        elif is_like == 0:
            for x in data:
                if x == 'main_id':
                    items_arr = [y for y in data[x]]

        return list(set(items_arr))

    # 餘弦相似
    def cosine_similarity(self,v, w):
        re_val = 0
        # math.sqrt:平方根
        sqrt_dot = math.sqrt(self.dot(v, v) * self.dot(w, w))

        if sqrt_dot > 0:
            re_val = self.dot(v, w) / math.sqrt(self.dot(v, v) * self.dot(w, w))

        return re_val

    # 點乘積(內積)
    def dot(self,v, w):
        """v_1 * w_1 + ... + v_n * w_n"""
        return sum(v_i * w_i for v_i, w_i in zip(v, w))

    # 找出與某物件最類似的
    def most_similar_items_to(self,items_id,similarities,unique_items):
        pairs = [(unique_items[other_items_id], similarity)
                 for other_items_id, similarity in enumerate(similarities)
                 if items_id != other_items_id and similarity > 0]

        return sorted(pairs,
                      key=lambda pair: pair[1],
                      reverse=True)

    def most_similar_users_to(self,user_id,user_similarities):
        pairs = [(other_user_id, similarity)                      # find other
                 for other_user_id, similarity in                 # users with
                    enumerate(user_similarities[user_id])         # nonzero
                 if user_id != other_user_id and similarity > 0]  # similarity

        return sorted(pairs,                                      # sort them
                      key=lambda pair: pair[1],                   # most similar
                      reverse=True)                               # first

    # 基於項目推薦給User，大於0.5才推薦
    def item_based_to_user(self,user_id,user_items_vector,similarities,unique_items,users_items, include_current_items=False):
        # 把相似的物件累加起來
        suggestions = defaultdict(float)

        if len(user_items_vector) > 0:
            for item_id, is_like in enumerate(user_items_vector[user_id]):
                #print('item_id',user_items_vector[user_id])
                if is_like == 1 and len(similarities) > 0:
                    similar_likes = self.most_similar_items_to(item_id,similarities[user_id],unique_items)
                    #print('similarities[user_id]',similarities[user_id])
                    #print('users_items[user_id]',users_items[user_id])
                    for item, similarity in similar_likes:
                        #if(similarity < 1.0 and item not in users_items[user_id]):
                        suggestions[item] += similarity


        # 依據權重進行排序
        suggestions = sorted(suggestions.items(),
                             key=lambda pair: pair[1],
                             reverse=True)


        if include_current_items:
            return suggestions
        else:
            return [suggestion
                    for suggestion, weight in suggestions
                    if suggestion not in users_items[user_id] and float(weight) >= setting.similar_percent]

    # 基於User，大於0.5才推薦
    def user_based_suggestions(self,user_id, user_similarities,users_items,include_current_interests=False):
        # 把相似的物件累加起來
        suggestions = defaultdict(float)
        for other_user_id, similarity in self.most_similar_users_to(user_id,user_similarities):
            for interest in users_items[other_user_id]:
                suggestions[interest] += similarity

        # 依據權重進行排序
        suggestions = sorted(suggestions.items(),
                             key=lambda pair: pair[1],
                             reverse=True)

        if include_current_interests:
            return suggestions
        else:
            return [suggestion
                    for suggestion, weight in suggestions
                    if suggestion not in users_items[user_id] and float(weight) >= setting.similar_percent]

    # 取得主建物的值
    def get_description(self,description):
        items_str = str(description)
        items_str = items_str.split('坪')
        items_str = items_str[0].split('：')

        return (items_str[1] if items_str[1] else '')

    # 檢查是否有已經close的物件，若有則取相似度最高的物件替換
    def check_close(self,user_unid,items):
        # 該User是否有ex_record_items_obj紀錄
        chk_user_sql    =  "SELECT  `items` \
                            FROM    `ex_record_items_obj` \
                            WHERE   `user_id` = %s AND `is_like` = 3"
        self.execute(chk_user_sql,[user_unid])
        this_user_obj   = self.fetchall()

        if len(this_user_obj) > 0 and this_user_obj[0]['items']:
            this_user_obj   = this_user_obj[0]['items'].lstrip('[').rstrip(']').split(',')
        else:
            this_user_obj   = []

        chk_main_sql    =  "SELECT  `id`"

        this_user_obj   = list(map(lambda x: int(x), this_user_obj))

        # 該User有被記錄到有興趣的項目
        if sum(this_user_obj) > 0:
            key = 0
            for item in setting.care_list:
                # 檢查各個項目
                if item != 'description' and item != 'floor':
                    if item in setting.basic_list:
                        chk_main_sql   += ",`"+item+"`"
                    else:
                        chk_main_sql   += ",`"+item+"`" if this_user_obj[key] == 1 else ''
                    key += 1
                else:
                    key += 1
                    continue

        # 該User完全沒有有興趣的項目
        else:
            chk_main_sql   += ",`area`,`price`,`ping`,`type`,`room`"

        chk_main_sql   +=  ",`direction` FROM   `ex_main` "+\
                            "WHERE   `id` IN (" + ','.join(str(i) for i in items) + ") AND "+\
                                    "`is_closed` = 1"

        self.execute(chk_main_sql)
        this_user_mains = self.fetchall()

        for _,mains in enumerate(this_user_mains):
            fields_arr  = {}
            other_sql   = ''
            for x,key in enumerate(mains):
                if mains[key]:
                    # 固定值
                    if key in setting.similar_list:
                        if mains[key]:
                            if key == 'direction' and mains[key] in setting.care_list_direction:
                                fields_arr[key] = ' IN ('+','.join(setting.care_list_direction)+')'
                            else:
                                fields_arr[key] = '='+str(mains[key])

                    # 價格
                    elif key == 'price':
                        # 價格
                        if mains[key] <= 300:
                            other_sql += " AND `price` <= 300 "
                        elif 300 < mains[key] <= 600:
                            other_sql += " AND `price` BETWEEN 300 AND 600 "
                        elif 600 < mains[key] <= 1000:
                            other_sql += " AND `price` BETWEEN 600 AND 1000 "
                        elif 1000 < mains[key] <= 1500:
                            other_sql += " AND `price` BETWEEN 1000 AND 1500 "
                        elif 1500 < mains[key] <= 2000:
                            other_sql += " AND `price` BETWEEN 1500 AND 2000 "
                        elif mains[key] > 2000:
                            other_sql += " AND `price` > 2000 "
                    # 坪數
                    elif key == 'ping':
                        if mains[key] <= 20:
                            other_sql += " AND `ping` <= 20 "
                        elif 20 < mains[key] <= 30:
                            other_sql += " AND `ping` BETWEEN 20 AND 30 "
                        elif 30 < mains[key] <= 40:
                            other_sql += " AND `ping` BETWEEN 30 AND 40 "
                        elif 40 < mains[key] <= 50:
                            other_sql += " AND `ping` BETWEEN 40 AND 50 "
                        elif mains[key] > 50:
                            other_sql += " AND `ping` > 50 "
                    elif key in setting.range_list:
                        mains[key]  = float(mains[key])
                        diff        = (mains[key] * setting.range_percent)
                        start_val   = math.floor(mains[key] - diff) if (mains[key] - diff) >= 0 else 0
                        end_val     = math.ceil(mains[key] + diff) if (mains[key] + diff) >= 0 else 0

                        # 在意項目越小越好
                        if key in setting.care_list_small:
                            fields_arr[key] = " <= "+str(end_val)

                        # 在意項目越大越好
                        elif key in setting.care_list_max:
                            fields_arr[key] = " >= "+ str(start_val)

            # 取得相似的物件
            get_similar_sql     =  "SELECT  `id` "+\
                                   "FROM    `ex_main` "+\
                                   "WHERE   `is_closed` = 0 "

            for key,val in fields_arr.items():
                get_similar_sql+= ' AND `'+key+'`'+str(val)

            get_similar_sql    +=  ' AND `id` != '+str(mains['id']) + (other_sql if other_sql != '' else '')

            self.execute(get_similar_sql)
            get_similar = self.fetchall()

            for x in get_similar:
                    items.append(x['id'])

            items.remove(mains['id']);

        return list(set(items))

