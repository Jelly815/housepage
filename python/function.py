# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 00:58:08 2019

@author: Jelly
"""

from db_connect import DB_CONN 

class FUNC_CLASS(DB_CONN):
    def __init__(self):
        #super(FUNC_CLASS, self).__init__() 
        super().__init__()
        
    
    # 取得user的id
    def get_user_id(self,user):  
        user_id = ''
        user_sql = "SELECT `id` FROM `ex_user` WHERE `unid` = '" + user + "'"
    
        try: 
            self.execute(user_sql)
            user_id_arr = self.fetchone()
            user_id = str(user_id_arr['id']) if int(user_id_arr['id']) != 0 else ''
        except:
            user_id = 'exit'
        
        return user_id
    
    # 取得user的搜尋紀錄
    def get_this_user_search(self,user_id):
        user_record = {}
        
        if user_id != '':
            # 取得user 最後搜尋的條件
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
            # 取得user 經常搜尋的條件
            user_often_sql = """
                SELECT `area`,`price`,`ping`,`style`,`type` 
                FROM `ex_record` 
                WHERE `user_id` = %s 
                ORDER BY `times` DESC
                """
                
            try:
                self.execute(user_last_sql,[user_id,user_id])
                user_last_arr = self.fetchone()
                if(user_last_arr != None):
                    user_record['last_record'] = [user_last_arr['area'],user_last_arr['price'],user_last_arr['ping'],user_last_arr['style'],user_last_arr['type']]
            
            
                self.execute(user_often_sql,[user_id])
                user_often_arr = self.fetchone()
            
                if(user_often_arr != None):
                    user_record['often_record'] = [user_often_arr['area'],user_often_arr['price'],user_often_arr['ping'],user_often_arr['style'],user_often_arr['type']]
            
                #setting.db_cursor.close()
                #setting.db_conn.close()
            except:
                user_record = {}
                
        return user_record
    
    # 取得非user的相同的紀錄
    def get_same_record(self,user_id,record):
        record_arr = {}
        
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
            
        try:
            self.execute(record_sql,[user_id,record[0],record[1],record[2],record[3],record[4],2])
            record_arr = self.fetchall()
            
            #setting.db_cursor.close()
            #setting.db_conn.close()
        except:
            record_arr = {}
       
        return record_arr
    
    # 取得瀏覽物件的時間區間(單位:秒)
    def get_times_range(self,user_id,record):
        record_arr = {}
        
        record_sql = """
            SELECT stay.`stay_time`
            FROM `ex_record_items` items,`ex_record` record,
                 `ex_record_items_stay` stay
            WHERE items.`record_id` = record.`id` AND 
                  items.`user_id` = record.`user_id` AND
                  items.`id` = stay.`record_items_id` AND
                  record.`user_id` = %s AND 
                  record.`area`    = %s AND 
                  record.`price`   = %s AND 
                  record.`ping`    = %s AND 
                  record.`style`   = %s AND 
                  record.`type`    = %s AND 
                  record.`times`   > %s  
            """
            
        try:
            self.execute(record_sql,[user_id,record[0],record[1],record[2],record[3],record[4],2])
            record_arr = self.fetchall()
            
            #setting.db_cursor2.close()
            #setting.db_conn.close()
        except:
            record_arr = {}
       
        return record_arr
    
'''   
import function  
x = function.DB_CONN()

AA = x.execute("SELECT `id` FROM `ex_user` WHERE `unid` = 'm199cdc39ee6e65811960a187ccf1fcb9'")
rows = x.fetchall()    # get all selected rows, as Barmar mentioned
for r in rows:
    print(r)
'''