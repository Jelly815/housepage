import requests
import json
from bs4 import BeautifulSoup
from db_connect import DB_CONN
'''
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

for house in house_list:
    houseid = house['houseid'] if 'houseid' in house else ''
    data_list[houseid]      = {}

    data_list[houseid]['city']       = house['region_name'] if 'region_name' in house else ''
    data_list[houseid]['area']       = house['section_name'] if 'section_name' in house else ''
    data_list[houseid]['title']      = house['title'] if 'title' in house else ''
    data_list[houseid]['road']       = house['street_name'] if 'street_name' in house else house['address']
    data_list[houseid]['style']      = house['room'] if 'room' in house else ''
    data_list[houseid]['ping']       = house['area'] if 'area' in house else house['mainarea']
    data_list[houseid]['parking']    = house['has_carport'] if 'has_carport' in house else ''
    data_list[houseid]['age']        = house['houseage'] if 'houseage' in house else 0
    data_list[houseid]['floor']      = house['floor'] if 'floor' in house else ''
    data_list[houseid]['type']       = house['shape_name'] if 'shape_name' in house else house['build_purpose']
    data_list[houseid]['builder']    = house['company'] if 'company' in house else ''
    data_list[houseid]['unit']       = house['unitprice'] if 'unitprice' in house else ''
    data_list[houseid]['price']      = house['price'] if 'price' in house else 0
    data_list[houseid]['around']     = house['tag'] if 'tag' in house else ''
    data_list[houseid]['status']     = house['type'] if 'type' in house else ''
    data_list[houseid]['community']  = house['community_name'] if 'community_name' in house else ''
    
    
    if data_list[houseid]['status'] == '2':
        url = 'https://sale.591.com.tw/home/house/detail/2/{}.html'.format(houseid)
    elif data_list[houseid]['status'] == 8:
        url = 'https://newhouse.591.com.tw/home/housing/detail?new=2&hid={}'.format(houseid)

    content_res = requests.get(url, headers=headers)
    
    content_text = content_res.text
    
    soup = BeautifulSoup(content_text, 'html5lib')
    soup.prettify()

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
    
    
    if data_list[houseid]['status'] == '2':  
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
        data_list[houseid]['disc'] = []
        disc_tag = soup.find_all('div','detail-house-box')
        for disc in disc_tag: 
             data_list[houseid]['disc'].append(disc)

    elif data_list[houseid]['status'] == 8: 
        # 建商 
        build_tag = soup.find_all('div','build_data')
        for build in build_tag:
            build_li_list = build.find_all('li')
            for build_li in build_li_list:
                if build_li.contents[0].text == '投資建設':
                    data_list[houseid]['build'] = build_li.contents[1]
        
        # 坪數說明            
        data_list[houseid]['disc'] = []
        disc_tag = soup.find_all('div','detail_message_wrap')
        for disc in disc_tag: 
            build_plan = disc.find('div','build_plan')
            build_ul = disc.find('ul','stonefont')
            
            if build_ul != None:
                data_list[houseid]['build'] = build_ul
 '''            
db_conn = DB_CONN()    
print(db_conn)