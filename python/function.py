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

class FUNC_CLASS(DB_CONN):

    def __init__(self,user_id):
        super().__init__()
        # 項目總數
        self.items_len   = len(setting.similar_list + setting.range_list)
        self.user_id     = user_id
        # 取得A曾經評價低於普通的房子
        get_bad_houses  = self.get_bad_houses()
        self.bad_houses  = ','.join((str(num) for num in get_bad_houses))

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

    # 取得評分推薦權重
    def get_weight(self):
        re_main     = {}

        default_sql = """
            SELECT  (CASE WHEN  ROUND(SUM(`math_`), 2) > 1 THEN 1
                    ELSE ROUND(SUM(`math_`), 2) END) AS 'weight'
            FROM   `ex_score_analysis`
            WHERE """

        #like_sql    = default_sql + " `type_` = 'like' AND `value_` >= 3"

        user_sql    = default_sql + " `type_` = 'user' AND `value_` >= 3"

        nolike_sql  = default_sql + " `type_` = 'nolike' AND `value_` >= 3"

        content_sql = default_sql + " `type_` = 'content' AND `value_` >= 3"

        hot_sql     = default_sql + " `type_` = 'hot' AND `value_` >= 3"

        new_sql     = default_sql + " `type_` = 'new' AND `value_` >= 3"

        search_sql  = default_sql + " `type_` = 'search' AND `value_` >= 3"

        try:
            #self.execute(like_sql,[])
            #like_sql_arr = self.fetchall()
            #re_main['like'] = like_sql_arr[0]['weight'] if like_sql_arr[0]['weight'] else 0

            self.execute(user_sql,[])
            user_sql_arr = self.fetchall()
            re_main['user'] = user_sql_arr[0]['weight'] if user_sql_arr[0]['weight'] else 0

            self.execute(nolike_sql,[])
            nolike_sql_arr = self.fetchall()
            re_main['nolike'] = nolike_sql_arr[0]['weight'] if nolike_sql_arr[0]['weight'] else 0

            self.execute(content_sql,[])
            content_sql_arr = self.fetchall()
            re_main['content'] = content_sql_arr[0]['weight'] if content_sql_arr[0]['weight'] else 0

            self.execute(hot_sql,[])
            hot_sql_arr = self.fetchall()
            re_main['hot'] = hot_sql_arr[0]['weight'] if hot_sql_arr[0]['weight'] else 0

            self.execute(new_sql,[])
            new_sql_arr = self.fetchall()
            re_main['new'] = new_sql_arr[0]['weight'] if new_sql_arr[0]['weight'] else 0

            self.execute(search_sql,[])
            search_sql_arr = self.fetchall()
            re_main['search'] = search_sql_arr[0]['weight'] if search_sql_arr[0]['weight'] else 0

            re_main     = sorted(re_main.items(),
                            key=lambda pair: pair[1],
                            reverse=True)
        except:
            re_main = []

        return re_main

    # 取得A曾經評價不喜歡的房子
    def get_bad_houses(self):
        re_main     = []
        user_sql    = """
                SELECT  `main_id`
                FROM    `ex_score`
                WHERE   `user_id` = %s AND
                        `score` = 1
                """

        try:
            self.execute(user_sql,[self.user_id])
            user_main_arr = self.fetchall()

            re_main = [x['main_id'] for x in user_main_arr]

        except:
            re_main = []

        return re_main

    # 取得A曾經搜尋過的條件
    def get_user_all_record(self,date_time=0):
        user_record = []
        time_str    = ''
        if self.user_id != '':
            try:
                where       = [self.user_id]

                if date_time == 1:
                    time_sql=   "SELECT `last_time` "+\
                                "FROM `ex_record` "+\
                                "WHERE `user_id`= %s "+\
                                "ORDER BY `last_time` DESC LIMIT 1"
                    self.execute(time_sql,[self.user_id])
                    time_arr    = self.fetchall()
                    time_str    = time_arr[0]['last_time']

                record_sql  = """
                    SELECT  DISTINCT `area`
                    FROM    `ex_record`
                    WHERE   `user_id` = %s AND
                    """

                record_sql  += " `last_time` = '"+str(time_str)+"'" if str(time_str) != '' else " `last_time` BETWEEN (NOW() - INTERVAL "+str(setting.search_house_days)+" DAY) AND NOW()"
                self.execute(record_sql,where)
                area_arr    = self.fetchall()
                area_arr    = [x['area'] for x in area_arr]

                record_sql  = """
                    SELECT  DISTINCT `price`
                    FROM    `ex_record`
                    WHERE   `user_id` = %s AND
                    """
                record_sql  += " `last_time` = '"+str(time_str)+"'" if str(time_str) != '' else " `last_time` BETWEEN (NOW() - INTERVAL "+str(setting.search_house_days)+" DAY) AND NOW()"
                self.execute(record_sql,where)
                price_arr   = self.fetchall()
                price_arr   = [x['price'] for x in price_arr]

                record_sql  = """
                    SELECT  DISTINCT `ping`
                    FROM    `ex_record`
                    WHERE   `user_id` = %s AND
                    """
                record_sql  += " `last_time` = '"+str(time_str)+"'" if str(time_str) != '' else " `last_time` BETWEEN (NOW() - INTERVAL "+str(setting.search_house_days)+" DAY) AND NOW()"
                self.execute(record_sql,where)
                ping_arr    = self.fetchall()
                ping_arr    = [x['ping'] for x in ping_arr]

                record_sql  = """
                    SELECT  DISTINCT `style`
                    FROM    `ex_record`
                    WHERE   `user_id` = %s AND
                    """
                record_sql  += " `last_time` = '"+str(time_str)+"'" if str(time_str) != '' else " `last_time` BETWEEN (NOW() - INTERVAL "+str(setting.search_house_days)+" DAY) AND NOW()"
                self.execute(record_sql,where)
                style_arr   = self.fetchall()
                style_arr   = [x['style'] for x in style_arr]

                record_sql  = """
                    SELECT  DISTINCT `type`
                    FROM    `ex_record`
                    WHERE   `user_id` = %s AND
                    """
                record_sql  += " `last_time` = '"+str(time_str)+"'" if str(time_str) != '' else " `last_time` BETWEEN (NOW() - INTERVAL "+str(setting.search_house_days)+" DAY) AND NOW()"
                self.execute(record_sql,where)
                type_arr    = self.fetchall()
                type_arr    = [x['type'] for x in type_arr]

                user_record = [area_arr,price_arr,ping_arr,style_arr,type_arr]
            except:
                user_record = []

        return user_record

    def get_user_all_record_items(self,user_all_record,recommand_items,orderby=''):
        area_str    = ','.join(str(num) for num in user_all_record[0]) if len(user_all_record) > 0 else ''
        style_str   = ','.join(str(num) for num in user_all_record[3]) if len(user_all_record[3]) > 0 else ''
        type_str    = ','.join(str(num) for num in user_all_record[4]) if len(user_all_record[4]) > 0 else ''
        id_str      = ','.join(str(num) for num in recommand_items) if len(recommand_items) > 0 else ''

        hot_house_sql  = "SELECT  `id` FROM `ex_main` WHERE `is_closed` = 0 AND "

        hot_house_sql += '`area` IN ('+area_str+') AND ' if area_str != '' else ''
        #價格
        num     = 0
        num2    = 0
        price_arr   = {'300':'0','600':'300','1000':'600','1500':'1000','2000':'1500','2001':''}
        if len(user_all_record[1]) == 1:
            if user_all_record[1][0] == '2001':
                num  = user_all_record[1][0]
                num2 = '5000'
            else:
                num  = price_arr[str(user_all_record[1][0])]
                num2 = user_all_record[1][0]
        else:
            for x in user_all_record[1]:
                if num == 0 and num2 == 0:
                    num  = x
                    num2 = x
                elif x > num2:
                    num2 = x
                else:
                    num  = x
        hot_house_sql += '`price` BETWEEN '+str(num)+' AND '+str(num2)+' AND ' if len(user_all_record[1]) > 0 else ''

        #坪數
        num     = 0
        num2    = 0
        ping_arr    = {'20':'0','30':'20','40':'30','50':'40','51':''}
        if len(user_all_record[2]) == 1:
            if user_all_record[2][0] == '51':
                num  = user_all_record[2][0]
                num2 = '100'
            else:
                num  = ping_arr[str(user_all_record[2][0])]
                num2 = user_all_record[2][0]
        else:
            for x in user_all_record[2]:
                if num == 0 and num2 == 0:
                    num  = x
                    num2 = x
                elif x > num2:
                    num2 = x
                else:
                    num  = x
        hot_house_sql += '`ping` BETWEEN '+str(num)+' AND '+str(num2)+' AND ' if len(user_all_record[2]) > 0 else ''

        hot_house_sql += '`room` IN ('+style_str+') AND ' if style_str != '' else ''
        hot_house_sql += '`type` IN ('+type_str+') AND ' if type_str != '' else ''
        hot_house_sql += '`id` IN ('+id_str+') AND ' if id_str != '' else ''
        hot_house_sql  = hot_house_sql.rstrip('AND ')

        if orderby != '':
            hot_house_sql  += orderby

        self.execute(hot_house_sql,[])
        result  = self.fetchall()
        result  = [x['id'] for x in result]

        return result

    # 取得user的搜尋紀錄(喜歡)
    def get_this_user_search(self):
        user_record = {}
        user_record['last_record']  = []
        user_record['often_record'] = []

        if self.user_id != '':
            user_sql    = """
                SELECT  `area`,`price`,`ping`,`style`,`type`
                FROM    `ex_record`
                WHERE   `user_id` = %s AND
                        `last_time` BETWEEN (NOW() - INTERVAL %s DAY) AND NOW()
                """

            try:
                # 取得user [最後]搜尋的條件
                self.execute(user_sql+" ORDER BY `last_time` DESC,times DESC LIMIT 1",\
                    [self.user_id,setting.search_house_days])
                user_last_arr = self.fetchall()

                if(user_last_arr is not None):
                    for x, last in enumerate(user_last_arr):
                        user_record['last_record'].append([last['area'],last['price'],last['ping'],last['style'],last['type']])

                # 取得user [經常]搜尋的條件
                self.execute(user_sql+" GROUP by  `area`,`price`,`ping`,`style`,`type` \
                    ORDER BY `times` DESC,`last_time` DESC,`price`,`ping` DESC LIMIT 3",\
                    [self.user_id,setting.search_house_days])
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
    def get_this_user_no_search(self):
        user_recommend  = []

        if self.user_id != '':
            # 取得user半年內的搜尋紀錄
            user_today_sql = """
                SELECT  `area`,`price`,`ping`,`style`,`type`
                FROM    `ex_user_record_view_not`
                WHERE   `user_id` = %s AND
                        `last_time` BETWEEN (NOW() - INTERVAL %s DAY) AND NOW()
                GROUP BY `area`,`price`,`ping`,`style`,`type`
                ORDER BY `last_time` DESC
                """
            try:
                self.execute(user_today_sql,[self.user_id,setting.search_house_days])
                user_today_arr  = self.fetchall()
                users   = []
                if len(user_today_arr) > 0:
                    for x, user_today in enumerate(user_today_arr):
                        record  = [user_today['area'],user_today['price'],user_today['ping'],user_today['style'],user_today['type']]

                        # 取得非user有一樣不喜歡記錄的人
                        users.extend(val['user_id'] for y,val in enumerate(self.get_same_record(self.user_id,record,1,1)))

                    users       = list(set(users))
                    if len(users) > 0:
                        for unid in users:
                            # 取得非user喜歡的房子
                            times_range_items   = self.get_times_range_items(unid,record)

                            if times_range_items:
                                user_recommend.extend(times_range_items)
            except:
                user_recommend = []

        return list(set(user_recommend))

    # 依內容比對(喜歡)(排除評價不好的)
    def get_this_user_content(self,users_items):
        user_recommend  = []
        users_items     = ','.join(str(num) for num in users_items) if users_items != '' else '0'

        if self.user_id != '':
            # 取得ex_user_record_view半年內的搜尋紀錄
            user_today_sql = """
                SELECT  `area`,`price`,`ping`,`style`,`type`,`main_id`
                FROM    `ex_user_record_view`
                WHERE   `user_id` = %s AND
                        `last_time` BETWEEN (NOW() - INTERVAL %s DAY) AND NOW()
                """
            user_today_sql += ' AND `main_id` IN ('+users_items+')'+\
                                ' ORDER BY `last_time` DESC'

            # ex_record_items_stay 半年內的搜尋紀錄
            user_stay_sql = """
                SELECT `type_key`,`type_value`
                FROM `ex_record_items` items,`ex_record_items_stay` stay
                WHERE `items`.`id` = `stay`.`record_items_id` and
                      `items`.`user_id` = %s AND
                      `stay`.`type_key` != 'stay_time' AND
                      `items`.`last_time` BETWEEN (NOW() - INTERVAL %s DAY) AND NOW()
                """

            try:
                self.execute(user_today_sql,[self.user_id,setting.search_house_days])
                user_today_arr  = self.fetchall()
                #print(user_today_arr)
                self.execute(user_stay_sql,[self.user_id,setting.search_house_days])
                user_stay_arr   = self.fetchall()
                #print(user_stay_arr)
                stay_count_arr  = {}
                stay_count      = 0
                for _,x in enumerate(user_stay_arr):
                    stay_count += x['type_value']
                    if stay_count_arr.get(x['type_key']):
                        stay_count_arr[x['type_key']] += x['type_value']
                    else:
                        stay_count_arr[x['type_key']] = x['type_value']

                stay_count_arr  = sorted(stay_count_arr.items(),
                                                key=lambda pair: pair[1],
                                                reverse=True)

                user_items_arr  = {}
                # 如果在意項目大於0 和 大於瀏覽房子數，才列入他有此習慣
                if len(stay_count_arr) > 0 and stay_count >= len(user_today_arr):
                    # 計算平均數
                    stay_avg    = math.ceil(stay_count/len(stay_count_arr))
                    # 取得在意項目
                    stay_count_arr      = [x[0] for _,x in enumerate(stay_count_arr) if x[1] >= stay_avg]
                    # 加上基本搜尋項目
                    stay_count_arr      = set(stay_count_arr+setting.basic_list)

                    for x in stay_count_arr:
                        user_items_arr[x] = []
                else:
                    user_items_arr      = {
                        'area':[],'road':[],'room':[],
                        'ping':[],'parking':[],
                        'type':[],'direction':[],
                        'price':[],'status':[]
                    }

                if len(user_today_arr) > 0:
                    user_today_sql  = 'SELECT  '

                    if len(user_items_arr.keys()) > 0:
                        for x in user_items_arr.keys():
                            user_today_sql += '`'+x+'`,'

                    user_today_sql  = user_today_sql.rstrip(',') + ' FROM `ex_main` WHERE `id` = %s'
                    #print('user_today_sql',user_today_sql)
                    for x, user_today in enumerate(user_today_arr):
                        self.execute(user_today_sql,[user_today['main_id']])
                        this_user_mains = self.fetchall()

                        for x,val in enumerate(this_user_mains):
                            new_row = list(val)
                            #print(new_row)
                            for i in new_row:
                                    if i == 'description':  #主建物坪數
                                        user_items_arr[i].append("")
                                    elif val[i] is not None:
                                        user_items_arr[i].append(val[i])

                    #print(user_items_arr)
                    new_val = {}
                    if len(user_items_arr['area']) > 0:

                        for item_type,record_items in  user_items_arr.items():
                            if item_type == 'area' and len(record_items) == 0:
                                continue
                            elif item_type in setting.out_items:
                                continue

                            new_val[item_type] = []

                            # 比對是否有一樣的
                            if item_type in setting.similar_list and len(record_items) > 0:
                                chk = {}
                                item_len = len(record_items)
                                #print(record_items)
                                # 計算項目的次數
                                for x in record_items:
                                    if chk.get(x):
                                        chk[x] += 1
                                    else:
                                        chk[x] = 1

                                # 依設定similar_percent列入該項目是否為喜歡
                                suggestions = sorted(chk.items(),
                                                key=lambda pair: pair[1],
                                                reverse=True)
                                #print(suggestions)
                                suggestion = [x[0]
                                        for x in suggestions
                                        if int(x[1]) >= int(item_len / len(suggestions))]
                                #print(suggestions)
                                new_val[item_type].extend(suggestion)
                            # 比對是否在範圍內
                            elif item_type in setting.range_list and len(record_items) > 0:
                                values      = list(map(lambda x: float(x), record_items))

                                # 計算平均值(this user)
                                mean_num_user   = np.mean(values)

                                # 價格
                                if item_type == 'price':
                                    if mean_num_user <= 300:
                                        user_val = [0,300]
                                    elif 300 < mean_num_user <= 600:
                                        user_val = [300,600]
                                    elif 600 < mean_num_user <= 1000:
                                        user_val = [600,1000]
                                    elif 1000 < mean_num_user <= 1500:
                                        user_val = [1000,1500]
                                    elif 1500 < mean_num_user <= 2000:
                                        user_val = [1500,2000]
                                    elif mean_num_user > 2000:
                                        user_val = [2000,5000]

                                    new_val[item_type].extend(user_val)
                                elif item_type == 'ping':
                                    #坪數
                                    if mean_num_user <= 20:
                                        user_val = [0,20]
                                    elif 20 < mean_num_user <= 30:
                                        user_val = [20,30]
                                    elif 30 < mean_num_user <= 40:
                                        user_val = [30,40]
                                    elif 40 < mean_num_user <= 50:
                                        user_val = [40,50]
                                    elif mean_num_user > 50:
                                        user_val = [51,100]

                                    new_val[item_type].extend(user_val)
                                else:
                                    # 計算標準差
                                    std_num     = np.std(record_items)
                                    # 如果只有一筆資料
                                    if std_num == 0:
                                        std_num = int(record_items[0] * setting.range_percent)

                                    # 計算範圍值
                                    star_num    = int(mean_num_user - std_num)
                                    end_num     = int(mean_num_user + std_num)

                                    new_val[item_type].extend([star_num,end_num])
                #print(new_val)
                # 依照內容，找到喜愛的物件
                where_sql   = ''
                length      = 1
                for x,items in new_val.items():
                    if x in setting.similar_list:
                        where_sql += ' `'+x+'` IN ('+','.join(str(e) for e in items)+') '
                    elif x in setting.range_list:
                        where_sql += ' `'+x+'` BETWEEN '+str(items[0])+' AND '+str(items[1])

                    where_sql += ' AND ' if length < len(new_val) else ''
                    length += 1

                # 尋找相似的房子
                user_record_sql =   'SELECT  `id` '+\
                                    'FROM    `ex_main` '+\
                                    'WHERE '+where_sql+' AND `id` NOT IN ('+(self.bad_houses+','+users_items if self.bad_houses != '' else users_items)+')'+\
                                    ' AND `is_closed` = 0'
                try:
                    self.execute(user_record_sql,[])
                    user_record_arr     = self.fetchall()

                    user_recommend = [int(x['id']) for x in user_record_arr]
                except:
                    user_record_arr     = {}
            except:
                user_recommend = []

        return list(set(user_recommend))

    # 取得非user有相同記錄的人
    def get_same_record(self,user_id,record,limit=1,notlike = 0):
        record_arr  = {}

        db_str      = '`ex_user_record_view_not`' if notlike == 1 else '`ex_record`'
        # 取得user record
        record_sql  = "SELECT  `user_id` FROM "+ db_str+ " WHERE   `user_id` != %s AND "+\
                        "`area`    = %s AND "+\
                        "`price`   = %s AND "+\
                        "`ping`    = %s AND "+\
                        "`style`   = %s AND "+\
                        "`type`    = %s"

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

    # 取得某位User瀏覽物件的資料(排除評價不好的)
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

        record_sql = """
            SELECT  `user_id`,`record_times`,`main_id`,`items_times`,`click_map`,
                    `add_favorite`,`item_stay_time`
            FROM    `ex_user_record_view`
            WHERE   `user_id` = %s
            """
        record_sql += (' AND `main_id` NOT IN ('+self.bad_houses+')' if self.bad_houses != '' else '') +\
            ' ORDER BY `item_stay_time`'

        record_vals = [user_id]
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

        #sug_len     = int(len(suggestions) * setting.similar_percent)
        #suggestions = suggestions[:sug_len]
        #if include_current_interests:
        #    return suggestions
        #else:
        return [suggestion
                for suggestion, weight in suggestions
                if suggestion not in users_items[user_id] and weight > setting.similar_percent]

    # 取得主建物的值
    def get_description(self,description):
        items_str = str(description)
        items_str = items_str.split('坪')
        items_str = items_str[0].split('：')

        return (items_str[1] if items_str[1] else '')

    # 檢查是否有已經close的物件，若有則取相似度最高的物件替換
    def check_close(self,user_unid,items):
        user_today_sql = "SELECT `id` FROM `ex_main` WHERE `id` IN "+\
                        "("+','.join(str(i) for i in items)+") AND `is_closed` = 1"

        try:
            self.execute(user_today_sql,[])
            user_today_arr      = self.fetchall()
            close_id    = [x['id'] for x in user_today_arr]

            for x in close_id:
                items.remove(x);
        except:
            user_recommend = []

        return list(set(items))