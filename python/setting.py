# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 00:28:45 2019

@author: Jelly
"""

import mysql.connector

db_conn = mysql.connector.connect(
  host="localhost",       
  user="root",    
  passwd="root",  
  database="myweb",
  buffered=True
)
 
db_cursor = db_conn.cursor(buffered=True,dictionary=True)
db_cursor2 = db_conn.cursor(buffered=True)
# 搜尋紀錄的次數，不可以小於search_times
search_times = '2'