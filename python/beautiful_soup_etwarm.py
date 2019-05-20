import requests
import json
from bs4 import BeautifulSoup
from db_connect import DB_CONN
import uuid
import hashlib
import datetime
import math

#台灣房屋
#url = 'http://www.twhg.com.tw/damian/getRandom4objectsWithVR.php?a=0.029526889365504738&city=%E9%AB%98%E9%9B%84%E5%B8%82'
#東森房屋
for page in range(21, 27):
    url = 'https://www.etwarm.com.tw/houses/buy-list-json?area=%E9%AB%98%E9%9B%84%E5%B8%82%E6%96%B0%E8%88%88%E5%8D%80-%E9%AB%98%E9%9B%84%E5%B8%82%E5%89%8D%E9%87%91%E5%8D%80-%E9%AB%98%E9%9B%84%E5%B8%82%E8%8B%93%E9%9B%85%E5%8D%80-%E9%AB%98%E9%9B%84%E5%B8%82%E9%B9%BD%E5%9F%95%E5%8D%80-%E9%AB%98%E9%9B%84%E5%B8%82%E4%B8%89%E6%B0%91%E5%8D%80-%E9%AB%98%E9%9B%84%E5%B8%82%E5%89%8D%E9%8E%AE%E5%8D%80-%E9%AB%98%E9%9B%84%E5%B8%82%E9%BC%93%E5%B1%B1%E5%8D%80-%E9%AB%98%E9%9B%84%E5%B8%82%E6%A5%A0%E6%A2%93%E5%8D%80-%E9%AB%98%E9%9B%84%E5%B8%82%E5%B0%8F%E6%B8%AF%E5%8D%80-%E9%AB%98%E9%9B%84%E5%B8%82%E5%B7%A6%E7%87%9F%E5%8D%80-%E9%AB%98%E9%9B%84%E5%B8%82%E4%BB%81%E6%AD%A6%E5%8D%80-%E9%AB%98%E9%9B%84%E5%B8%82%E5%B2%A1%E5%B1%B1%E5%8D%80-%E9%AB%98%E9%9B%84%E5%B8%82%E8%B7%AF%E7%AB%B9%E5%8D%80-%E9%AB%98%E9%9B%84%E5%B8%82%E9%B3%B3%E5%B1%B1%E5%8D%80-%E9%AB%98%E9%9B%84%E5%B8%82%E5%A4%A7%E5%AF%AE%E5%8D%80-%E9%AB%98%E9%9B%84%E5%B8%82%E7%87%95%E5%B7%A2%E5%8D%80-%E9%AB%98%E9%9B%84%E5%B8%82%E6%A9%8B%E9%A0%AD%E5%8D%80-%E9%AB%98%E9%9B%84%E5%B8%82%E6%97%97%E6%B4%A5%E5%8D%80-%E9%AB%98%E9%9B%84%E5%B8%82%E7%BE%8E%E6%BF%83%E5%8D%80-%E9%AB%98%E9%9B%84%E5%B8%82%E6%97%97%E5%B1%B1%E5%8D%80&type=1-2-3-4-5-6&price1=100&price2=1500&ping1=10&ping2=50&sort=DEFAULT&page='+str(page)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    response = requests.get(url, headers=headers)
    #response = requests.post(url)

    json_text = response.text
    #json_text = json_text.encode("utf8").decode("cp950", "ignore")
    data = json.loads(json_text)

    house_list = data['data']
    data_list = {}

    for house in house_list:
        houseid = house['編號'] if '編號' in house else ''

        data_list[houseid]      = {}

        data_list[houseid]['source']     = 3
        data_list[houseid]['city']       = house['縣市'] if '縣市' in house else ''
        data_list[houseid]['area']       = house['鄉鎮市區'] if '鄉鎮市區' in house else ''
        data_list[houseid]['title']      = house['案名'] if '案名' in house else ''
        data_list[houseid]['road']       = house['地址'] if '地址' in house else house['addr']

        if '格局' in house and len(house['格局']) > 0:
            if isinstance(house['格局'],dict):
                for key, value in house['格局'].items():
                    if key == 0:
                        data_list[houseid]['room'] = value
                    else:
                        data_list[houseid]['room'] = '0房'
            else:
                data_list[houseid]['room']   = house['格局'][0]
        else:
            data_list[houseid]['room']   = '0房'

        data_list[houseid]['style']      = house['格局'] if '格局' in house else '0;'
        data_list[houseid]['ping']       = house['總坪數'] if '總坪數' in house else 0
        data_list[houseid]['parking']    = house['車位'] if '車位' in house else ''
        data_list[houseid]['age']        = house['屋齡'] if '屋齡' in house else 0
        data_list[houseid]['floor']      = ''
        data_list[houseid]['type']       = house['物件類別'] if '物件類別' in house else ''
        data_list[houseid]['direct']     = house['座向'] if '座向' in house else 0
        data_list[houseid]['fee']        = 0
        data_list[houseid]['builder']    = ''
        data_list[houseid]['unit']       = house['每坪單價'] if '每坪單價' in house else ''
        data_list[houseid]['price']      = house['刊登售價'] if '刊登售價' in house else 0
        data_list[houseid]['description']      = house['特色推薦'] if '特色推薦' in house else ''
        data_list[houseid]['status']     = 4
        data_list[houseid]['community']  = ''

        url = 'https://www.etwarm.com.tw/houses/buy/{}'.format(houseid)

        content_res = requests.get(url, headers=headers)

        content_text = content_res.text

        soup = BeautifulSoup(content_text, 'html5lib')
        soup.prettify()

        #生活機能
        num = 0
        data_list[houseid]['around'] = []
        around_tag = soup.find_all('div','object-data-box')
        for around in around_tag:
            if num == 2:
                around_tag2 = around.find('div','col-md-4 d-table')
                child = around.findChildren('div')
                num1 = 0

                if child[0].find('div').text == '捷運站名':
                    data_list[houseid]['around'].extend([child[0].find('div').find_next_sibling('div').text])
                if child[7].find('div').text == '鄰近商圈':
                    data_list[houseid]['around'].extend([child[7].find('div').find_next_sibling('div').text])
                if child[10].find('div').text == '鄰近學校':
                    data_list[houseid]['around'].extend([child[10].find('div').find_next_sibling('div').text])

            num = num + 1

        data_list[houseid]['img']      = house['多媒體']['照片'] if '多媒體' in house else ''

    #---------- 匯入資料庫 ----------#
    db_conn     = DB_CONN()
    select_sql  ="SELECT `number` FROM `ex_main` WHERE `number` = %s"

    md5         = hashlib.md5()

    # 縣市
    db_conn.execute("SELECT `id`,`name` FROM `ex_area` WHERE `disable` = 0")
    area_arr = db_conn.fetchall()
    area_list = {}
    for area in area_arr:
        area_list[area['name']] = area['id']

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
                `direction`, `fee`, `builder`, `unit`, `price`, `description`,
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
                    if vals == '大樓':
                        vals = 3
                    elif type_list[vals]:
                        vals = type_list[vals]
                    insert_vals.append(vals)
                elif key == 'city' or key == 'area':
                    insert_vals.append(area_list[vals])
                elif key == 'room':
                    #print(vals)
                    insert_vals.append(vals[0])
                elif key == 'style':
                    style = ''
                    if isinstance(vals,dict):
                        for x,value in vals.items():
                            style += value[0]+';'
                    else:
                        for x in vals:
                            style += x[0]+';'
                    insert_vals.append(style)
                elif key == 'parking':
                    insert_vals.append(1 if vals != '' else 0)
                elif key == 'age':
                    insert_vals.append(vals[:-1])
                elif key == 'direct':
                    direct = [direct_key  for (direct_key, direct_val) in direction_list.items() if direct_val == vals]
                    insert_vals.append(int(direct[0]) if direct else '')
                elif key == 'unit':
                    vals = vals[1:]
                    vals = vals[:-4]
                    insert_vals.append(vals)
                elif key == 'img':
                    for url in vals:
                        insert_imgs_sql += " (%s,%s),"
                        insert_imgs_vals.extend([houseid,url])
                elif key == 'around':
                    around = ''
                    if vals[1] != '－':
                        around += '2;'
                    if vals[2] != '－':
                        around += '5;'
                    if vals[0] != '－':
                        around += '15;'
                    insert_vals.append(around)
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