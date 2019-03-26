# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 00:58:08 2019

@author: Jelly
"""

from db_connect import DB_CONN
import setting
import math
#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
import time
import datetime

class FUNC_CLASS(DB_CONN):

    def __init__(self):
        super().__init__()

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

    # 取得user的搜尋紀錄
    def get_this_user_search(self,user_id):
        user_record = {}
        user_record['last_record']  = []
        user_record['often_record'] = []

        if user_id != '':
            # 取得user 最後搜尋的條件
            user_last_sql = """
                SELECT `area`,`price`,`ping`,`style`,`type`
                FROM `ex_user_record_view`
                WHERE `user_id` = %s
                ORDER BY `last_time` DESC LIMIT 1
                """

            # 取得user 經常搜尋的條件
            user_often_sql = """
                SELECT `area`,`price`,`ping`,`style`,`type`
                FROM `ex_record`
                WHERE `user_id` = %s
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

                    # 取得該範圍內，User有加入最愛的物件
                    is_favorite_items = self.get_is_favorite(new_arr,['main_id','add_favorite','item_stay_time'],user_time_range)


                    # 查看是否曾經看過地圖

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
            hot_house_vals = [record[0]]
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
                        `ping` = %s AND
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
    def get_is_favorite(self,data,columns_list,time_range):
        items_arr   = []
        df = pd.DataFrame(data, columns=columns_list)
        df = df[df['item_stay_time'] >= time_range]
        df_favorite = df[df.add_favorite == 1]

        # 如果有加入最愛，則把該物件加入list
        if not df_favorite.empty:
            for x in df_favorite.index:
                items_arr.append(df['main_id'][x])
        else:
            items_arr = df.main_id
        return list(set(items_arr))

    # 餘弦相似
    def cosine_similarity(self,v, w):
        # math.sqrt:平方根
        return self.dot(v, w) / math.sqrt(self.dot(v, v) * self.dot(w, w))

    # 點乘積(內積)
    def dot(self,v, w):
        """v_1 * w_1 + ... + v_n * w_n"""
        return sum(v_i * w_i for v_i, w_i in zip(v, w))