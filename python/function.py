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
        user_last_sql = """
            SELECT `area`,`price`,`ping`,`style`,`type` 
            FROM `ex_record` record 
            WHERE `user_id` = %s AND `id` = (
                   SELECT `record_id` 
                   FROM `ex_record_items` 
                   WHERE  `user_id` = record.`user_id` AND 
                          `user_id` = %s 
                   ORDER BY `last_time` DESC LIMIT 1)
            """
        setting.db_cursor.execute(user_last_sql,[user_id,user_id])
        user_last_arr = setting.db_cursor.fetchone()
        if(user_last_arr != None):
            user_record['last_record'] = [user_last_arr['area'],user_last_arr['price'],user_last_arr['ping'],user_last_arr['style'],user_last_arr['type']]
        
        # 取得user 經常搜尋的條件
        user_often_sql = """
            SELECT `area`,`price`,`ping`,`style`,`type` 
            FROM `ex_record` 
            WHERE `user_id` = %s 
            ORDER BY `times` DESC
            """
        setting.db_cursor.execute(user_often_sql,[user_id])
        user_often_arr = setting.db_cursor.fetchone()
        
        if(user_often_arr != None):
            user_record['often_record'] = [user_often_arr['area'],user_often_arr['price'],user_often_arr['ping'],user_often_arr['style'],user_often_arr['type']]
    
    return user_record

# 取得非user的相同的紀錄
def get_same_record(user_id,record):
    user_record = {}
    
    # 取得user record
    record_sql = """
        SELECT `user_id` 
        FROM `ex_record` 
        WHERE   `user_id` != %s AND 
                `area`  = %s AND 
                `price` = %s AND 
                `ping`  = %s AND 
                `style` = %s AND 
                `type`  = %s AND 
                `times` > %s
        """
    setting.db_cursor.execute(record_sql,[user_id,record[0],record[1],record[2],record[3],record[4],setting.search_times])
    record_arr = setting.db_cursor.fetchall()
   
    print(record_sql)
    return record_arr