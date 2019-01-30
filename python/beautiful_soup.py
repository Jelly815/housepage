import requests
import json
from bs4 import BeautifulSoup
from db_connect import DB_CONN
import uuid
import hashlib
import datetime
import math

db_conn = DB_CONN() 

url = 'https://sale.591.com.tw/home/search/list?type=2&&shType=list&regionid=17&firstRow=0&totalRows=14679&timestamp=1548122419382'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
response = requests.get(url, headers=headers)

json_text = response.text
json_text = json_text.encode("utf8").decode("cp950", "ignore")
data = json.loads(json_text)

house_list = data['data']['house_list']
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

    data_list[houseid]['source']     = 1 if status == 2 else 2
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
        data_list[houseid]['description'] = []
        disc_tag = soup.find('div','detail-house-box')
 
        if disc_tag != None:
            data_list[houseid]['description'] = disc_tag
                
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
        data_list[houseid]['description'] = []
        disc_tag = soup.find_all('div','detail_message_wrap')
        for disc in disc_tag: 
            build_plan = disc.find('div','build_plan')
            build_ul = disc.find('ul','stonefont')
            
            if build_ul != None:
                data_list[houseid]['description'] = build_ul
        
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
    data_list[houseid]['around']     = ''.join(str(x)+';' for x in around_str)
    data_list[houseid]['status']     = 4 if status == 2 else 3
    data_list[houseid]['community']  = house['community_name'] if 'community_name' in house else ''
    
    # 圖片
    data_list[houseid]['img'] = []
    photo_tag = soup.find_all('div', id='img_list')
    
    for tag in photo_tag:
        tdTags = tag.find_all("img")
        
        for tag in tdTags:
            if data_list[houseid]['status'] == '2':
                data_list[houseid]['img'].append(tag.get('src').replace('_118x88.crop','_730x460.water3'))
            elif data_list[houseid]['status'] == 8:
                data_list[houseid]['img'].append(tag.get('src').replace('_104x78.crop','_560x420.crop.water1'))
                
#print(data_list)
          
   
"""
data_list = {
    109791: {'city': '高雄市', 'area': '仁武區', 'title': '得邑巨商', 'road': '仁雄路206號', 'room': '5', 
             'style': '5~7房', 'ping': 145, 'parking': '', 'age': 0, 'floor': '', 'type': '透天', 
             'direct': '', 'fee': 0, 'builder': '得邑建設', 'unit': 0, 'price': 5680, 
             'description': '''<ul class="clearfix stonefont">

                                                    <li><span>結構工程</span>暫無                            </li>
                            <li><span>用途規劃</span>住家用</li>
                            <li><span>棟戶規劃</span><em title="7戶店面">7戶店面</em></li>
                            <li><span>土地分區</span>暫無</li>
                            <li><span>樓層規劃</span>地上5層</li>
                            <li><span>停車方式</span>前院停車</li>
                            <li><span>房數規劃</span>5~7房</li>
                            <li><span>管理費用</span>待定</li>
                            <li><span>寬深規劃</span>面寬6.00米、縱深0.00米</li>
                            <li>
                                <span style="float: left;">基地面積</span>
                                570坪                                                            </li>
                            <li>
                                <span>交屋屋況</span>
                                標準配備</li>
                            <li>
                                <span>建  蔽  率 </span>
                                38.07%<i class="fa fa-question-circle fa_tooltip" data-placement="top" data-toggle="tooltip" title="指建築基地上，建物的最大投影面積與建築基地面積的比值。"></i>                                                            </li>
                                                    <li class="orientation"><span>座向規劃</span>朝南</li>
                            <li class="building_materials">
                                <span>建材說明</span>
                                <strong>
                                    暫無                                </strong>
                            </li>
                                                </ul>''', 
            'around': ['新成屋', '住家用', '景觀宅', '近公園', '重劃區'], 'status': 8, 'community': '', 
            'img': ['https://hp1.591.com.tw/house/active/2017/02/14/148704480196598901_560x420.crop.water1.jpg', 
                    'https://hp1.591.com.tw/house/active/2017/02/14/148704530169230706_560x420.crop.water1.jpg', 
                    'https://hp1.591.com.tw/house/active/2017/02/14/148704482262286206_560x420.crop.water1.jpg', 
                    'https://hp1.591.com.tw/house/active/2017/02/14/148704496994558008_560x420.crop.water1.jpg', 
                    'https://hp1.591.com.tw/house/active/2017/02/14/148704526074760406_560x420.crop.water1.jpg']}, 

5901255: {'city': '高雄市', 'area': '楠梓區', 'title': '德賢商圈裝潢典雅大露臺漂亮三房平車', 'road': '德豐街', 'room': '3', 
          'style': '3房2廳2衛', 'ping': 42.31, 'parking': 1, 'age': 7, 'floor': '2F/15F', 'type': '電梯大樓', 'direct': '',
          'fee': '1948', 'builder': '', 'unit': '16.5', 'price': 698, 
          'description': '''<div class="detail-house-box">
                    <div class="detail-house-name">房屋資料</div>
                    <div class="detail-house-content">
                                                                                <div class="detail-house-item">
                                <div class="detail-house-key">現況</div>
                                <span>：</span>
                                <div class="detail-house-value">住宅</div>
                            </div>
                                                                                                            <div class="detail-house-item">
                                <div class="detail-house-key">型態</div>
                                <span>：</span>
                                <div class="detail-house-value">電梯大樓</div>
                            </div>
                                                                                                            <div class="detail-house-item">
                                <div class="detail-house-key">裝潢程度</div>
                                <span>：</span>
                                <div class="detail-house-value">簡易裝潢</div>
                            </div>
                                                                                                            <div class="detail-house-item">
                                <div class="detail-house-key">管理費</div>
                                <span>：</span>
                                <div class="detail-house-value">1948元</div>
                            </div>
                                                                                                            <div class="detail-house-item">
                                <div class="detail-house-key">帶租約</div>
                                <span>：</span>
                                <div class="detail-house-value">否</div>
                            </div>
                                                                                                            <div class="detail-house-item">
                                <div class="detail-house-key">法定用途</div>
                                <span>：</span>
                                <div class="detail-house-value">住家用</div>
                            </div>
                                                                                                            <div class="detail-house-item">
                                <div class="detail-house-key">公設比</div>
                                <span>：</span>
                                <div class="detail-house-value">33%</div>
                            </div>
                                                                        </div>
                </div>''', 
                'around': ['含車位', '有陽台'], 'status': '2', 'community': '大河苑', 
                'img': ['https://hp2.591.com.tw/house/active/2019/01/23/154821633781419601_730x460.water3.jpg', 
                        'https://hp2.591.com.tw/house/active/2019/01/23/154821634543668907_730x460.water3.jpg', 
                        'https://hp2.591.com.tw/house/active/2019/01/23/154821635222372408_730x460.water3.jpg', 
                        'https://hp2.591.com.tw/house/active/2019/01/23/154821635952661400_730x460.water3.jpg', 
                        'https://hp2.591.com.tw/house/active/2019/01/23/154821636734645601_730x460.water3.jpg', 
                        'https://hp2.591.com.tw/house/active/2019/01/23/154821637521874306_730x460.water3.jpg', 
                        'https://hp2.591.com.tw/house/active/2019/01/23/154821638251277803_730x460.water3.jpg', 
                        'https://hp2.591.com.tw/house/active/2019/01/23/154821638648616703_730x460.water3.jpg', 
                        'https://hp2.591.com.tw/house/active/2019/01/23/154821639382573706_730x460.water3.jpg', 
                        'https://hp2.591.com.tw/house/active/2019/01/23/154821639750914607_730x460.water3.jpg', 
                        'https://hp2.591.com.tw/house/active/2019/01/23/154821640025236107_730x460.water3.jpg', 
                        'https://hp2.591.com.tw/house/active/2019/01/23/154821652863918706_730x460.water3.jpg', 
                        'https://hp2.591.com.tw/house/active/2019/01/23/154821652543375302_730x460.water3.jpg']}, 

5768006: {'city': '高雄市', 'area': '三民區', 'title': '【陽明國中文山全新宅】雙套房有平車', 'road': '文揚街', 'room': '4', 
          'style': '4房2廳3衛', 'ping': 86.22, 'parking': 1, 'age': 5, 'floor': '2F/20F', 'type': '電梯大樓', 
          'direct': '坐西朝東', 'fee': '6328', 'builder': '', 'unit': '19.69', 'price': 1698, 
          'description': '''<div class="detail-house-box">
                    <div class="detail-house-name">房屋資料</div>
                    <div class="detail-house-content">
                                                                                <div class="detail-house-item">
                                <div class="detail-house-key">現況</div>
                                <span>：</span>
                                <div class="detail-house-value">住宅</div>
                            </div>
                                                                                                            <div class="detail-house-item">
                                <div class="detail-house-key">型態</div>
                                <span>：</span>
                                <div class="detail-house-value">電梯大樓</div>
                            </div>
                                                                                                            <div class="detail-house-item">
                                <div class="detail-house-key">裝潢程度</div>
                                <span>：</span>
                                <div class="detail-house-value">尚未裝潢</div>
                            </div>
                                                                                                            <div class="detail-house-item">
                                <div class="detail-house-key">管理費</div>
                                <span>：</span>
                                <div class="detail-house-value">6328元</div>
                            </div>
                                                                                                            <div class="detail-house-item">
                                <div class="detail-house-key">帶租約</div>
                                <span>：</span>
                                <div class="detail-house-value">否</div>
                            </div>
                                                                                                            <div class="detail-house-item">
                                <div class="detail-house-key">法定用途</div>
                                <span>：</span>
                                <div class="detail-house-value">住家用</div>
                            </div>
                                                                                                            <div class="detail-house-item">
                                <div class="detail-house-key">公設比</div>
                                <span>：</span>
                                <div class="detail-house-value">36%</div>
                            </div>
                                                                        </div>
                </div>''', 
                'around': ['明星學區', '含車位', '有陽台'], 'status': '2', 'community': '湖立方.文山特區', 
                'img': ['https://hp1.591.com.tw/house/active/2018/07/21/153216214123682208_730x460.water3.jpg', 
                        'https://hp2.591.com.tw/house/active/2018/12/13/154467950471760703_730x460.water3.jpg', 
                        'https://hp2.591.com.tw/house/active/2018/12/13/154467907868856706_730x460.water3.jpg', 
                        'https://hp1.591.com.tw/house/active/2018/07/21/153216214274307703_730x460.water3.jpg', 
                        'https://hp1.591.com.tw/house/active/2018/07/21/153216216058762808_730x460.water3.jpg', 
                        'https://hp1.591.com.tw/house/active/2018/07/21/153216219594363504_730x460.water3.jpg', 
                        'https://hp2.591.com.tw/house/active/2018/12/13/154467949386031401_730x460.water3.jpg', 
                        'https://hp2.591.com.tw/house/active/2018/12/13/154467952915338605_730x460.water3.jpg', 
                        'https://hp1.591.com.tw/house/active/2018/07/21/153216214959833002_730x460.water3.jpg', 
                        'https://hp2.591.com.tw/house/active/2018/12/13/154467870016132400_730x460.water3.jpg', 
                        'https://hp2.591.com.tw/house/active/2018/12/13/154467912770769005_730x460.water3.jpg', 
                        'https://hp2.591.com.tw/house/active/2018/12/13/154467884137320900_730x460.water3.jpg', 
                        'https://hp2.591.com.tw/house/active/2018/12/13/154467917732124000_730x460.water3.jpg', 
                        'https://hp1.591.com.tw/house/active/2019/01/05/154666725492750503_730x460.water3.jpg']}
}
"""
insert_sql  ='''
            INSERT INTO `ex_main`
            (`unid`, `number`,`source`, `city`, `area`, `title`,`road`,
             `room`, `style`, `ping`, `parking`, `age`, `floor`, `type`, 
            `direction`, `fee`, `builder`, `unit`, `price`, `description`, 
            `around`, `status`, `community`, `view_num`, `add_time`, 
             `is_closed`) VALUES 
            '''

select_sql  ="SELECT `number` FROM `ex_main` WHERE `number` = %s"

insert_vals = []
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
                break
            elif key == 'city':
                city = [area_key  for (area_key, area_val) in area_list.items() if area_val == vals]
                insert_vals.append(int(city[0]) if city else '')
            elif key == 'area':
                area = [area_key  for (area_key, area_val) in area_list.items() if area_val == vals]
                insert_vals.append(int(area[0]) if area else '')
            elif key == 'type':
                type_ = [type_key  for (type_key, type_val) in type_list.items() if type_val == vals]
                insert_vals.append(int(type_[0]) if type_ else '')
            elif key == 'direct':
                direct = [direct_key  for (direct_key, direct_val) in direction_list.items() if direct_val == vals]
                insert_vals.append(int(direct[0]) if direct else '')
            elif key == 'around':
                around_str = ''
                for around in vals:
                    around_str += around + ';'
                insert_vals.append(around_str)
            else:
                insert_vals.append(vals)
    
        insert_vals.extend([0,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),0])
        
insert_sql = insert_sql.rstrip(',')    
print(insert_vals)
#db_conn.execute(insert_sql,insert_vals)
