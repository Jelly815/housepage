# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 00:28:45 2019

@author: Jelly
"""

# 搜尋紀錄的次數，不可以小於search_times
search_times 	= 1

# 瀏覽時間不可低於view_seconds，單位:秒
view_seconds 	= 5

# 設定尋找房子的時間(預設6個月)，單位:天(60*60*24*180)
search_house_days = 180

# 範圍內百分比
range_percent 	= 0.1

# 相似的項目
similar_list 	= ["community","status","builder","direction","type","floor","parking","room","area"]
# 範圍的項目
range_list 		= ["description","price","unit","fee","age","ping"]

# 基本搜尋項目
basic_list 		= ["area","price","ping","room","type"]

# 在意項目設定
care_list		= ["community","status","description","price","unit","builder","fee","direction","type","floor","age","parking","ping","room","area"]
# 在意項目類似值
care_list_direction	= [["1","5"],["2","6"],["3","8"],["4","7"]]
# 在意項目越小越好
care_list_small	= ["price","unit","fee","age"]
# 在意項目越大越好
care_list_max	= ["description","ping"]

# 相似度百分比
similar_percent = 0.5

# 當推薦物件少於幾筆時，要加入User所在區域熱門的物件
less_how_num 	= 10

# 隨機取得要推薦的數量
random_num 		= 5