# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 00:58:08 2019

@author: Jelly
"""

import setting

# 取得user的id
def get_user_id(user):    
    user_sql = "SELECT `id` FROM `ex_user` WHERE `unid` = '" + user + "'"
    setting.db_cursor.execute(user_sql)
    user_id_arr = setting.db_cursor.fetchone()
    user_id = str(user_id_arr['id']) if int(user_id_arr['id']) != 0 else ''
    
    return user_id

# 取得user的搜尋紀錄
def get_this_user_search(user_id):
    user_record = {}
    
    # 取得user 最後搜尋的條件
    if user_id != '':
        user_last_sql = "SELECT `record_id` FROM `ex_record_items` WHERE `user_id` = " + user_id + " ORDER BY `last_time` DESC"
        setting.db_cursor.execute(user_last_sql)
        user_last_arr = setting.db_cursor.fetchone()
        user_last_record = str(user_last_arr['record_id']) if int(user_last_arr['record_id']) != 0 else ''
        
        if user_last_record != '':
            user_record_sql = "SELECT * FROM `ex_record` WHERE `user_id` = " + user_id + " AND `id` = " + user_last_record
            setting.db_cursor.execute(user_record_sql)
            user_record_arr = setting.db_cursor.fetchone()
            if(user_record_arr != None):
                user_record['last_record'] = [user_record_arr['area'],user_record_arr['price'],user_record_arr['ping'],user_record_arr['style'],user_record_arr['type']]

        # 取得user 經常搜尋的條件
        user_often_sql = "SELECT * FROM `ex_record` WHERE `user_id`=" + user_id + " ORDER BY `times` DESC"
        setting.db_cursor.execute(user_often_sql)
        user_often_arr = setting.db_cursor.fetchone()
        
        if(user_often_arr != None):
            user_record['often_record'] = [user_often_arr['area'],user_often_arr['price'],user_often_arr['ping'],user_often_arr['style'],user_often_arr['type']]
    
    return user_record

# 取得非user的相同的紀錄
def get_same_record(user_id,record):
    user_record = {}
    
    # 取得user record
    record_sql = "SELECT `user_id` FROM `ex_record` WHERE `user_id` != " + user_id + " AND `area`=" + str(record[0]) + " AND `price`=" + str(record[1]) + " AND `ping` =" + str(record[2]) + " AND `style`= " + str(record[3]) + " AND `type`=" + str(record[4]) + " AND `times` > " + setting.search_times
    setting.db_cursor.execute(record_sql)
    record_arr = setting.db_cursor.fetchall()
   
    print(record_sql)
    return record_arr