import requests
import json
from bs4 import BeautifulSoup
from db_connect import DB_CONN
import uuid
import hashlib
import datetime
import math
db_conn = DB_CONN()

#url = 'https://sale.591.com.tw/home/search/list?type=2&&shType=list&regionid=17&firstRow=60&totalRows=14679&timestamp=1548122419382'
#url = 'https://sale.591.com.tw/home/search/list?type=2&&shType=list&regionid=17&price=100$_2000$&order=posttime_desc&firstRow=60&totalRows=12671&timestamp=1549086616121'
url = 'https://sale.591.com.tw/home/search/list?type=2&&shType=list&regionid=17&section=268&price=690$_845$&area=29$_36$&timestamp=1556122918428'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

#response = requests.get(url, headers=headers)

#json_text = response.text

#json_text = json_text.encode("utf8").decode("cp950", "ignore")
#data = json.loads(json_text)

#house_list = data['data']['house_list']
house_list = [{\
"address": "建國路三段319巷",\
"area": 30.77,\
"browsenum": 32,\
"cartmodel": "",\
"carttype": "",\
"community_link": "",\
"community_name": "文山藏美",\
"delivery": "",\
"fci_pai": "",\
"floor": "9F/15F",\
"has_carport": 1,\
"houseage": 2,\
"houseid": 6206138,\
"is_carport": "0",\
"is_combine": 0,\
"is_down_price": 0,\
"is_hurry_price": 0,\
"is_oversea": "0",\
"is_video": 0,\
"isnew": 0,\
"isvip": 0,\
"kind": 9,\
"kind_name": "住宅",\
"mainarea": 14.06,\
"nick_name": "仲介蕭小姐",\
"photoNum": 11,\
"photo_url": "https://hp2.591.com.tw/house/active/2019/02/21/155073762941038701_208x156.crop.jpg",\
"posttime": 1556004644,\
"price": 728,\
"refreshtime": "52分鐘內",\
"region_name": "高雄市",\
"room": "2房2廳1衛",\
"saletype": 0,\
"section_name": "鳳山區",\
"shape_name": "電梯大樓",\
"showhouseage": "2年",\
"showprice": "728",\
"tag": [],\
"title": "文山藏美2房平移車位",\
"type": "2",\
"unit_price": "23.66萬/坪",\
"unitprice": "23.66"
}]
data_list = {}

db_conn = DB_CONN()

#生活機能
db_conn.execute("SELECT `id`,`name` FROM `ex_around`")
around_arr = db_conn.fetchall()
around_list = {}
for around in around_arr:
    around_list[around['id']] = around['name']

for house in house_list:

    houseid = house['houseid'] if 'houseid' in house else ''
    status  = house['type'] if 'type' in house else ''
    data_list[houseid]      = {}

    data_list[houseid]['source']     = 1 if status == '2' else 2
    data_list[houseid]['city']       = house['region_name'] if 'region_name' in house else ''
    data_list[houseid]['area']       = house['section_name'] if 'section_name' in house else ''
    data_list[houseid]['title']      = house['title'] if 'title' in house else ''
    data_list[houseid]['road']       = house['street_name'] if 'street_name' in house else house['address']

    if 'room' in house and house['room'] != '':
        data_list[houseid]['room']   = house['room'][0] if house['room'][0].isdigit() else 0
    else:
        data_list[houseid]['room']   = 0

    data_list[houseid]['style']      = house['room'] if 'room' in house else ''
    data_list[houseid]['ping']       = house['area'] if 'area' in house else house['mainarea']
    data_list[houseid]['parking']    = house['has_carport'] if 'has_carport' in house else ''
    data_list[houseid]['age']        = house['houseage'] if 'houseage' in house else 0
    data_list[houseid]['floor']      = house['floor'] if 'floor' in house else ''
    data_list[houseid]['type']       = house['shape_name'] if 'shape_name' in house else house['build_purpose']
    data_list[houseid]['direct']     = ''
    data_list[houseid]['fee']        = 0
    data_list[houseid]['builder']    = house['company'] if 'company' in house else ''
    data_list[houseid]['unit']       = house['unitprice'] if 'unitprice' in house else ''
    data_list[houseid]['price']      = house['price'] if 'price' in house else 0

    if status == '2':
        url = 'https://sale.591.com.tw/home/house/detail/2/{}.html'.format(houseid)
    elif status == 8:
        url = 'https://newhouse.591.com.tw/home/housing/detail?new=2&hid={}'.format(houseid)

    content_res = requests.get(url, headers=headers)

    content_text = content_res.text

    soup = BeautifulSoup(content_text, 'html5lib')
    soup.prettify()

    around_str = []

    if status == '2':
        # 朝向
        addr_tag = soup.find_all('div', class_='info-addr-content')
        for one in addr_tag:
            key_vals = one.find_all('span',class_='info-addr-key')
            for key in key_vals:
                if key.get_text() == '朝向':
                    this_vals = key.find_next_siblings('span')
                    data_list[houseid]['direct'] = this_vals[0].text
                    break

        # 管理費
        fee_tag = soup.find_all('div','detail-house-key')
        for fee in fee_tag:
             if fee.text == '管理費':
                 this_fee = fee.find_next_siblings('div')
                 data_list[houseid]['fee'] = this_fee[0].text.replace('元','') if this_fee[0].text != '無' else ''

        # 坪數說明
        data_list[houseid]['description'] = ''
        disc_tag = soup.find('div','detail-house-box')

        if disc_tag != None:
            data_list[houseid]['description'] = str(disc_tag)

        # 生活機能
        around_tag = soup.find_all('div','detail-house-life')
        for around in around_tag:
            for (around_key, around_val) in around_list.items():
                if around_val == around.text:
                    around_str.append(around_key)

    elif status == 8:
        # 建商
        #build_tag = soup.find_all('div','build_data')
        #for build in build_tag:
        #    build_li_list = build.find_all('li')
        #    for build_li in build_li_list:
        #        if build_li.contents[0].text == '投資建設':
        #            data_list[houseid]['build'] = build_li.contents[1]

        # 坪數說明
        data_list[houseid]['description'] = ''
        disc_tag = soup.find_all('div','detail_message_wrap')
        for disc in disc_tag:
            build_plan = disc.find('div','build_plan')
            build_ul = disc.find('ul','stonefont')

            if build_ul != None:
                data_list[houseid]['description'] = str(build_ul)

        # 生活機能
        tag_list = []
        if 'tag' in house:
            for tag in house['tag']:
                tag_list.append(tag)

                for around_key,around_val in around_list.items():

                    if around_val == tag:
                        tag_list.pop()
                        around_str.append(around_key)
                    elif len(tag_list) > 0:   # 比對文字
                        tag1    = set([tag[x] for x in range(len(tag))])
                        tag2    = set([around_val[x] for x in range(len(around_val))])
                        tag2_len= math.ceil(len(tag2)/2)

                        if len(tag2.difference(tag1)) < tag2_len:
                            tag_list.pop()
                            around_str.append(around_key)
                            break

        if len(tag_list) > 0:
            for val in tag_list:
                insert_around_sql = "REPLACE INTO `ex_around`(`name`) VALUES (%s)"
                db_conn.execute(insert_around_sql,[val])
                # 取得id
                db_conn.execute("SELECT `id` FROM `ex_around` WHERE `name` = %s ",[val])
                get_id = db_conn.fetchone()
                if get_id:
                    around_str.append(get_id['id'])

    around_str.sort()
    data_list[houseid]['around']     = ';'.join(str(x) for x in around_str) if around_str else ''
    data_list[houseid]['status']     = 4 if status == '2' else 3
    data_list[houseid]['community']  = house['community_name'] if 'community_name' in house else ''

    # 圖片
    data_list[houseid]['img'] = []
    photo_tag = soup.find_all('div', id='img_list')

    for tag in photo_tag:
        tdTags = tag.find_all("img")

        for tag in tdTags:
            if status == '2':
                data_list[houseid]['img'].append(tag.get('src').replace('_118x88.crop','_730x460.water3'))
            elif status == 8:
                data_list[houseid]['img'].append(tag.get('src').replace('_104x78.crop','_560x420.crop.water1'))

#---------- 匯入資料庫 ----------#
insert_sql  ='''
            INSERT INTO `ex_main`
            (`unid`, `number`,`source`, `city`, `area`, `title`,`road`,
             `room`, `style`, `ping`, `parking`, `age`, `floor`, `type`,
            `direction`, `fee`, `builder`, `unit`, `price`, `description`,
            `around`, `status`, `community`, `view_num`, `add_time`,
             `is_closed`) VALUES
            '''

select_sql  ="SELECT `number` FROM `ex_main` WHERE `number` = %s"

insert_imgs ="INSERT INTO `ex_images` (`number`,`img_url`) VALUES "

insert_vals = []
insert_imgs_vals = []
md5         = hashlib.md5()

# 縣市
db_conn.execute("SELECT `id`,`name` FROM `ex_area` WHERE `disable` = 0")
area_arr = db_conn.fetchall()
area_list = {}
for area in area_arr:
    area_list[area['id']] = area['name']

# 型態
db_conn.execute("SELECT `id`,`name` FROM `ex_type`")
type_arr = db_conn.fetchall()
type_list = {}
for type_ in type_arr:
    type_list[type_['id']] = type_['name']

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
        insert_sql += "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s),"

        uuid4   = uuid.uuid4()
        md5.update(str(uuid4).encode('utf-8'))

        insert_vals.extend([md5.hexdigest(),houseid])

        for key,vals in this_data.items():
            if key == 'img':

                for url in vals:
                    insert_imgs += "(%s,%s),"
                    insert_imgs_vals.extend([houseid,url])

            elif key == 'city':
                city = [area_key  for (area_key, area_val) in area_list.items() if area_val == vals]
                insert_vals.append(int(city[0]) if city else '')
            elif key == 'area':
                area = [area_key  for (area_key, area_val) in area_list.items() if area_val == vals]
                insert_vals.append(int(area[0]) if area else '')
            elif key == 'direct':
                direct = [direct_key  for (direct_key, direct_val) in direction_list.items() if direct_val == vals]
                insert_vals.append(int(direct[0]) if direct else '')
            else:
                insert_vals.append(vals)

        insert_vals.extend([0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),0])

insert_sql = insert_sql.rstrip(',')
insert_imgs = insert_imgs.rstrip(',')

if insert_vals:
    db_conn.execute(insert_sql,insert_vals)
    db_conn.execute(insert_imgs,insert_imgs_vals)
else:
    print("no insert")
