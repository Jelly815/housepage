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
import sys
import os
import time
import datetime
import re
from collections import defaultdict
import json

class FUNC_CLASS(DB_CONN):

    def __init__(self):
        super().__init__()
        # 項目總數
        self.items_len   = len(setting.similar_list + setting.range_list)

    # 取得user的id
    def get_user_id(self,user_unid):
        user_id     = 0
        user_sql    = "SELECT `id` FROM `ex_user` WHERE `unid` = %s"

        try:
            self.execute(user_sql,[user_unid])
            user_id_arr = self.fetchone()
            user_id = str(user_id_arr['id']) if int(user_id_arr['id']) != 0 else ''
        except:
            user_id = 0

        return user_id

    # 取得最早的上線時間
    def get_user_login_time(self):
        login_day = 0

        login_time_sql      = """
            SELECT  `login_time`
            FROM    `ex_user`
            ORDER BY `login_time`
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
            # 取得user 最後搜尋的條件
            user_last_sql = """
                SELECT  `area`,`price`,`ping`,`style`,`type`
                FROM    `ex_user_record_view`
                WHERE   `user_id` = %s
                ORDER BY `last_time` DESC LIMIT 1
                """

            # 取得user 經常搜尋的條件
            user_often_sql = """
                SELECT  `area`,`price`,`ping`,`style`,`type`
                FROM    `ex_record`
                WHERE   `user_id` = %s
                ORDER BY `times` DESC,`price`,`ping` DESC LIMIT 3
                """
            try:
                # 取得user [最後]搜尋的條件
                self.execute(user_last_sql,[user_id])
                user_last_arr = self.fetchall()

                if(user_last_arr is not None):
                    for x, last in enumerate(user_last_arr):
                        user_record['last_record'].append([last['area'],last['price'],last['ping'],last['style'],last['type']])

                # 取得user [經常]搜尋的條件
                self.execute(user_often_sql,[user_id])
                user_often_arr = self.fetchall()

                if user_often_arr is not None:
                    for x, often in enumerate(user_often_arr):
                        user_record['often_record'].append([often['area'],often['price'],often['ping'],often['style'],often['type']])
                        if user_record['last_record']:
                            diff = set(user_record['often_record'][x]).difference(set(user_record['last_record'][0]))

                        # 如果經常搜尋紀錄中有含最後的搜尋，則刪除最後搜尋的條件，避免重複物件出現
                        #if diff == set():
                            #user_record['last_record'] = []
            except:
                user_record = {}

        return user_record

    # 取得user的搜尋紀錄(不喜歡)
    def get_this_user_no_search(self,user_id):
        user_record = {}
        user_range  = {}
        user_recommend  = []
        if user_id != '':
            # 取得useritems_str 半年內的搜尋紀錄
            user_today_sql = """
                SELECT  `area`,`price`,`ping`,`style`,`type`,`main_id`
                FROM    `ex_user_record_view_not`
                WHERE   `user_id` = %s AND
                        `last_time` BETWEEN (NOW() - INTERVAL %s DAY) AND NOW()
                ORDER BY `last_time` DESC
                """

            try:
                self.execute(user_today_sql,[user_id,setting.search_house_seconds])
                user_today_arr  = self.fetchall()
                record_arr      = []
                if len(user_today_arr) > 0:
                    items_arr   = {
                            'area':[],'road':[],'room':[],
                            'ping':[],'parking':[],'age':[],
                            'floor':[],'type':[],'direction':[],
                            'fee':[],'builder':[],'unit':[],
                            'price':[],'description':[],'around':[],
                            'status':[],'community':[]
                    }

                    for x, user_today in enumerate(user_today_arr):
                        record  = [user_today['area'],user_today['price'],user_today['ping'],user_today['style'],user_today['type']]
                        record_arr.append(record)
                        users   = [val['unid'] for y,val in enumerate(self.get_same_record(user_id,record))]

                        #本User看過的物件資料
                        user_today_sql = """
                            SELECT  `community`,`status`,`around`,`description`,`price`,`unit`,`builder`,`fee`,
                                    `direction`,`type`,`floor`,`age`,`parking`,`ping`,`room`,`road`,`area`
                            FROM    `ex_main`
                            WHERE   `id` = %s AND `is_closed` = 0
                            """

                        self.execute(user_today_sql,[user_today['main_id']])

                        this_user_mains = self.fetchall()

                        for x,val in enumerate(this_user_mains):
                            new_row = list(val)
                            for i in new_row:
                                if i == 'description':  #主建物坪數
                                    items_str = str(val[i])
                                    items_str = items_str.split('坪')
                                    items_str = items_str[0].split('：')

                                    items_arr[i].append(items_str[1])
                                elif val[i] is not None:
                                    items_arr[i].append(val[i])

                        #找到其他User後，取出不喜歡的項目
                        for unid in users:
                            user_today_sql = """
                                SELECT  `items`
                                FROM    `ex_record_items_obj`
                                WHERE   `user_id` = %s AND `is_like` = 0
                                """
                            self.execute(user_today_sql,[unid])
                            other_user_nolike_json= self.fetchall()
                            user_record[unid] = json.loads(other_user_nolike_json[0]['items'])

                    for user_id,record_items in  user_record.items():
                        user_to_others = []

                        for key,values in record_items.items():

                            # 比對是否有一樣的
                            if key in setting.similar_list and len(values) > 0:
                                intersection = list(set(map(lambda x: str(x), items_arr[key])) & set(values))
                                percent = round((len(intersection) / len(items_arr[key])),3) if len(items_arr[key]) != 0 else 0

                                # 相似的大於一半才算
                                user_to_others.append(1 if len(intersection) > 0 and percent >= 0.5 else 0)

                            # 比對是否在範圍內
                            elif key in setting.range_list and len(values) > 0:
                                values      = list(map(lambda x: float(x), values))
                                items_arr[key]  = list(map(lambda x: float(x), items_arr[key]))
                                # 計算標準差
                                std_num     = np.std(values)
                                # 計算平均值
                                mean_num    = np.mean(values)

                                star_num    = std_num - mean_num
                                end_num     = std_num + mean_num

                                # 範圍內的大於一半才算
                                intersection= [1 if x >= star_num and x <= end_num else 0
                                               for x in items_arr[key]]
                                percent = round((sum(intersection) / len(items_arr[key])),3) if len(items_arr[key]) != 0 else 0

                                user_to_others.append(1 if len(intersection) > 0 and percent >= 0.5 else 0)

                        user_range[user_id] = round((sum(user_to_others) / self.items_len),3)

                # 找到的User，依照相似度高至低排序
                user_range  = sorted(user_range.items(), key=lambda d: d[1], reverse=True)

                # 依照搜尋紀錄、相似者，找到喜愛的物件
                # 是否要排除相似度小於50%的
                #*************紀錄不對，因為這邊的紀錄似乎是不喜歡物件的搜尋紀錄
                for this_record in record_arr:
                    for user in user_range:
                        # 取得A(喜愛)的物件(瀏覽時間大於5秒,瀏覽次數大於1or有加入最愛)
                        times_range_items = self.get_times_range_items(user[0],this_record)

                        if times_range_items:
                            for x in times_range_items:
                                user_recommend.append(x)
                print(user_recommend)
            except:
                user_recommend = []

        return list(set(user_recommend))

    # 取得非user的相同的紀錄
    def get_same_record(self,user_id,record,limit=1):
        record_arr = {}

        # 取得user record
        record_sql = """
            SELECT  user.`unid`
            FROM    `ex_user` user,`ex_record` record
            WHERE   user.`unid` = record.`user_id` AND
                    record.`user_id` != %s AND
                    record.`area`    = %s AND
                    record.`price`   = %s AND
                    record.`ping`    = %s AND
                    record.`style`   = %s AND
                    record.`type`    = %s AND
                    user.`login_time` >= (NOW() - INTERVAL %s DAY)
            """

        record_vals = [
                user_id,
                record[0],record[1],record[2],
                record[3],record[4],
                (int)(setting.search_house_seconds * limit)
        ]

        try:
            if(record):
                self.execute(record_sql,record_vals)
                record_arr = self.fetchall()
            else:
                # 若setting.search_house_seconds設定的天數找不到資料，則往回推天數，直到找到資料
                limit += 1

                login_last_day = self.get_user_login_time()
                if login_last_day > setting.search_house_seconds:
                    limit_round = int(login_last_day / setting.search_house_seconds)

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
                self.execute(record_sql,record_vals)
                record_arr = self.fetchall()

                if record_arr:
                    for _, record in enumerate(record_arr):
                        for key,val in record.items():
                            new_arr[key].append(val)

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
                    user_time_range = self.get_user_time_range(new_arr['item_stay_time'])

                    # 某user喜歡物件的時間圓餅圖
                    #if new_arr['item_stay_time']:
                    #    self.plt_pie(new_arr)

                    # 如果User有加入最愛的習慣1;反之0
                    is_like = 1 if sum(new_arr['add_favorite']) > 0 else 0

                    # 取得該範圍內，User有加入最愛的物件
                    is_favorite_items = self.get_is_favorite(new_arr,['main_id','add_favorite','item_stay_time'],user_time_range,is_like)
        except:
            is_favorite_items = []

        return is_favorite_items

    # 取得分類最熱門的房子(no_data=0，有1筆記錄；no_data=1:有1筆記錄，但資料不足；no_data=:完全沒資料)
    def get_hot_house(self,record,no_data=0,user_id=''):
        hot_house_vals = []
        hot_house_sql      = """
                SELECT  `id`
                FROM    `ex_main`
                WHERE   `area` = %s
                """

        if no_data == 1:
            hot_house_sql      += """
                        AND
                        `style`= %s AND
                        `is_closed` = 0
                ORDER BY `view_num`,`update_time`
                LIMIT 5
                """
            hot_house_vals = [record[0],record[3]]
        elif no_data == 2:
            user_area_sql = "SELECT `area_id` FROM `ex_user` WHERE unid = %s"
            self.execute(user_area_sql,[user_id])
            user_area      = self.fetchall()

            hot_house_sql      += """
                        AND
                        `is_closed` = 0
                ORDER BY `view_num`,`update_time`
                LIMIT 5
                """
            hot_house_vals = [user_area[0]['area_id']]
        else:
            hot_house_sql      += """
                        AND
                        `price`= %s AND
                        `ping` <= %s AND
                        `style`= %s AND
                        `type` = %s AND
                        `is_closed` = 0
                ORDER BY `view_num`,`update_time`
                """
            hot_house_vals = [record[0],record[1],record[2],record[3],record[4]]

        try:
            self.execute(hot_house_sql,hot_house_vals)
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
            # abs:絕對值;  abs(X - 平均值)
            df['x-Mean']    = abs(df[field] - df[field].mean())
            # std:標準差，有 95% 信心估計母群體平均數，在樣本平均數 ± 1.96 * (母群體標準差 / 樣本數 n 的平方根) 的範圍內。
            df['1.96*std']  = 1.96*df[field].std()
            df['Outlier']   = abs(df[field] - df[field].mean()) > 1.96*df[field].std()

            # 刪除為True的資料
            for x in range(len(df)):
                this_bool = df.iloc[x]['Outlier']
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
            items_arr   = [data[x] for x in data if x == 'main_id']

        return list(set(items_arr))

    # 餘弦相似
    def cosine_similarity(self,v, w):
        # math.sqrt:平方根
        return self.dot(v, w) / math.sqrt(self.dot(v, v) * self.dot(w, w))

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

    def item_based_to_user(self,user_id,user_items_vector,similarities,unique_items,users_items, include_current_items=False):
        # 把相似的物件累加起來
        suggestions = defaultdict(float)

        for item_id, is_like in enumerate(user_items_vector):
            if is_like == 1:
                similar_likes = self.most_similar_items_to(item_id,similarities,unique_items)
                for item, similarity in similar_likes:
                    suggestions[item] += similarity

        # 依據權重進行排序
        suggestions = sorted(suggestions.items(),
                             key=lambda pair: pair[1],
                             reverse=True)

        if include_current_items:
            return suggestions
        else:
            return [(suggestion, weight)
                    for suggestion, weight in suggestions
                    if suggestion not in users_items[user_id]]