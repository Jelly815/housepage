import requests
import json
from bs4 import BeautifulSoup
from db_connect import DB_CONN
import uuid
import hashlib
import datetime
import random
import time

for page in range(21, 40):
    time.sleep(5)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    payload = {
            'q': '2^1^18^^^^1^2_3_4_5^^1_10^^1_25^^^^^^^^^'+str(page)+'^0',
            'rlg': '1'
    }
    #住商不動產
    response = requests.post('http://www.hbhousing.com.tw/ajax/dataService.aspx?job=search&path=house', data = payload, headers=headers)
    
    #print(response.text)
    json_text = response.text
    data = json.loads(json_text)
    
    house_list = data['data']
    data_list = {}
    
    for house in house_list:
        houseid = house['s'] if 's' in house else ''
    
        data_list[houseid]      = {}
    
        data_list[houseid]['source']     = 4
        data_list[houseid]['city']       = 275
        data_list[houseid]['area']       = house['c'] if 'c' in house else ''
        data_list[houseid]['title']      = house['n'] if 'n' in house else ''
        data_list[houseid]['road']       = house['x'] if 'x' in house else house['addr']
    
        if 'p' in house and len(house['p']) > 0:
            if isinstance(house['p'],dict):
                for key, value in house['p'].items():
                    if key == 0:
                        data_list[houseid]['room'] = value
                    else:
                        data_list[houseid]['room'] = '0房'
            else:
                data_list[houseid]['room']   = house['p'][0]
        else:
            data_list[houseid]['room']   = '0房'
    
        data_list[houseid]['style']      = house['p'] if 'p' in house else '0;'
        data_list[houseid]['ping']       = house['a'] if 'a' in house else 0
        data_list[houseid]['parking']    = house['y'] if 'y' in house else ''
        data_list[houseid]['age']        = house['k'] if 'k' in house else 0
        data_list[houseid]['floor']      = house['w'] if 'w' in house else 0
        data_list[houseid]['type']       = house['t'] if 't' in house else ''
        data_list[houseid]['direct']     = 0
        data_list[houseid]['fee']        = 0
        data_list[houseid]['builder']    = ''
        data_list[houseid]['price']      = house['np'] if 'np' in house else 0
        data_list[houseid]['unit']       = (float(house['np']) / float(house['a']))  
        data_list[houseid]['description']      = house['g'] if 'g' in house else ''
        data_list[houseid]['status']     = 4
        data_list[houseid]['community']  = ''
        data_list[houseid]['around']     = house['mrt'] if 'mrt' in house else ''
        data_list[houseid]['img']        = house['i'] if 'i' in house else ''
 
    #---------- 匯入資料庫 ----------#
    db_conn     = DB_CONN()
    select_sql  ="SELECT `number` FROM `ex_main` WHERE `number` = %s"
    
    md5         = hashlib.md5()
    
    # 縣市
    db_conn.execute("SELECT `id`,`zip_code` FROM `ex_area` WHERE `disable` = 0")
    area_arr = db_conn.fetchall()
    area_list = {}
    for area in area_arr:
        area_list[area['zip_code']] = area['id']
    
    # 型態
    db_conn.execute("SELECT `id`,`name` FROM `ex_type`")
    type_arr = db_conn.fetchall()
    type_list = {}
    for type_ in type_arr:
        type_list[type_['name']] = type_['id']
    
    # 朝向
    db_conn.execute("SELECT `id`,`name` FROM `ex_direction`")
    direction_arr = db_conn.fetchall()
    direction_list = {}
    for direction in direction_arr:
        direction_list[direction['id']] = direction['name']
    
    # 塞值
    for houseid,this_data in data_list.items():
        db_conn.execute(select_sql,[houseid])
    
        if db_conn.fetchone() is None:
            insert_sql  ='''
                INSERT INTO `ex_main`
                (`unid`, `number`,`source`, `city`, `area`, `title`,`road`,
                 `room`, `style`, `ping`, `parking`, `age`, `floor`, `type`,
                `direction`, `fee`, `builder`, `price`,`unit`, `description`,
                `status`, `community`, `around`, `view_num`, `add_time`,
                 `is_closed`) VALUES
                (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                '''
            insert_imgs ="INSERT INTO `ex_images` (`number`,`img_url`) VALUES "
            insert_imgs_sql = ''
    
            uuid4   = uuid.uuid4()
            md5.update(str(uuid4).encode('utf-8'))
            insert_vals = []
            insert_imgs_vals = []
    
            insert_vals.extend([md5.hexdigest(),houseid])
    
            for key,vals in this_data.items():
                if key == 'type':
                    if vals == '大廈':
                        vals = 3
                    elif type_list[vals]:
                        vals = type_list[vals]
                    insert_vals.append(vals)
                elif key == 'area':
                    new_vals = vals.split("_")
                    insert_vals.append(area_list[int(new_vals[1])])
                elif key == 'style':
                    style = ''
                    if isinstance(vals,dict):
                        for x,value in vals.items():
                            style += value[0]+';'
                    elif isinstance(vals,str):
                        style = vals+';'
                    elif len(vals) > 0:
                        for x in vals:
                            style += str(x)+';' if x != '' else str(1)+';'
                    else:
                        style = ''
                    insert_vals.append(style)
                elif key == 'parking':
                    insert_vals.append(1 if vals != '' else 0)
                elif key == 'direct':
                    insert_vals.append(random.randint(1,8))
                elif key == 'img':
                    for url in vals:
                        insert_imgs_sql += " (%s,%s),"
                        insert_imgs_vals.extend([houseid,url])
                elif key == 'around':
                    vals = '1;2;4;5;15;' if vals != '' else '1;2;4;5;'
                    insert_vals.append(vals)
                else:
                    insert_vals.append(vals)
    
            insert_vals.extend([0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),0])
    
            if insert_vals:
                insert_sql = insert_sql.rstrip(',')
                insert_imgs = (insert_imgs+insert_imgs_sql).rstrip(',')
            
                db_conn.execute(insert_sql,insert_vals)
                db_conn.execute(insert_imgs,insert_imgs_vals)
            else:
                print(this_data['number'])