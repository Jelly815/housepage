import requests
import json
from bs4 import BeautifulSoup
from db_connect import DB_CONN
"""
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
                data_list[houseid]['disc'] = build_ul
                
print(data_list)
"""            
db_conn = DB_CONN()    

data_list = {
116237: {
    'city': '高雄市', 'area': '鳳山區', 'title': '中山極上', 'road': '五甲三路295巷17號', 
    'style': '', 'ping': 0, 'parking': '', 'age': 0, 'floor': '', 'type': '住宅大樓', 
    'builder': '宏城建設股份有限公司', 'unit': 25, 'price': 0, 
    'around': ['新成屋', '住家用', '捷運宅', '明星學區', '景觀宅'], 
    'status': 8, 'community': '', 
    'img': [
        'https://hp1.591.com.tw/house/active/2018/03/13/152092855417848501_560x420.crop.water1.jpg', 
        'https://hp1.591.com.tw/house/active/2018/03/13/152092861908372807_560x420.crop.water1.jpg', 
        'https://hp1.591.com.tw/house/active/2018/03/13/152092871019579308_560x420.crop.water1.jpg', 
        'https://hp1.591.com.tw/house/active/2018/03/13/152092857688248404_560x420.crop.water1.jpg', 
        'https://hp1.591.com.tw/house/active/2018/03/13/152092878568845406_560x420.crop.water1.jpg', 
        'https://hp1.591.com.tw/house/active/2018/03/13/152092884921421500_560x420.crop.water1.jpg'], 
    'build': '宏城建設股份有限公司', 
    'disc': '''<ul class="clearfix stonefont">
               <li><span>公  設  比</span>35.98%<i class="fa fa-question-circle fa_tooltip" data-placement="top" data-toggle="tooltip" title="為建物權狀中共用部分的持分坪數/建物總坪數"></i></li>
                            <li><span>棟戶規劃</span><em title="1棟，22戶住家">1棟，22戶住家</em></li>
                            <li>
                                <span style="float: left;">建  蔽  率 </span>
                                52.01%<i class="fa fa-question-circle fa_tooltip" data-placement="top" data-toggle="tooltip" title="指建築基地上，建物的最大投影面積與建築基地面積的比值。"></i>                                                            </li>
                            <li><span>樓層規劃</span>地上12層，地下3層</li>
                            <li><span>車位規劃</span>平面式27個</li>
                            <li><span>管理費用</span>80元/坪/月</li>
                            <li><span>車位配比</span>1:1.23<i class="fa fa-question-circle fa_tooltip" data-placement="top" data-toggle="tooltip" title="每位住戶可以分配到的車位數"></i></li>
                            <li><span>結構工程</span>RC
              <i class="fa fa-question-circle fa_tooltip" data-placement="top" data-toggle="tooltip" title="鋼筋混凝土結構"></i>
              </li>
                            <li>
                                <span style="float: left;">基地面積</span>
                                303.11坪                                                            </li>
                            <li><span>用途規劃</span>住家用</li>
                            <li><span>交屋屋況</span>標準配備</li>
                            <li><span>土地分區</span>第三之一種住宅區</li>
                                                        <li class="orientation"><span>座向規劃</span>朝西南</li>
                            <li class="building_materials">
                                <span>建材說明</span>
                                <strong>
                                    主臥採TOTO全自動馬桶，TOTO暖房四合一乾燥機，ROCA浴缸，大雅廚具，櫻花牌影藏式抽油煙機，BOSCH崁入式烤箱。                                </strong>
                            </li>
                                                            <li class="facility">
                                    <span>公共設施</span>
                                    <div class="facility_box">
                                                                                    <i class="icon_1">接待大廳</i>                                                                                    <i class="icon_4">空中花園</i>                                                                                    <i class="icon_6">交誼廳</i>                                                                                    <i class="icon_7">會議室</i>                                                                                    <i class="icon_8">閱覽室</i>                                                                                    <i class="icon_9">視聽室</i>                                                                                    <i class="icon_23">信箱區</i>                                                                                    <i class="icon_24">曬被區</i>                                                                            </div>
                                </li>
                                                </ul>'''}, 
5768006: {'city': '高雄市', 'area': '三民區', 'title': '【陽明國中文山全新宅】雙套房有平車', 
          'road': '文揚街', 'style': '4房2廳3衛', 'ping': 86.22, 'parking': 1, 'age': 5, 
          'floor': '2F/20F', 'type': '電梯大樓', 'builder': '', 'unit': '19.69', 'price': 1698, 
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
                  'https://hp1.591.com.tw/house/active/2019/01/05/154666725492750503_730x460.water3.jpg'], 
         'direct': '坐西朝東', 'fee': '6328', 
         'disc': ['''<div class="detail-house-box">
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
                </div>, <div class="detail-house-box">
                    <div class="detail-house-name">坪數說明</div>
                    <div class="detail-house-content">
                                                    <div class="detail-house-item">
                                <div class="detail-house-key">主建物</div>
                                <span>：</span>
                                <div class="detail-house-value">45.23坪</div>
                            </div>
                                                    <div class="detail-house-item">
                                <div class="detail-house-key">共用部分</div>
                                <span>：</span>
                                <div class="detail-house-value">27.87坪</div>
                            </div>
                                                    <div class="detail-house-item">
                                <div class="detail-house-key">附屬建物</div>
                                <span>：</span>
                                <div class="detail-house-value">4.9坪</div>
                            </div>
                                                    <div class="detail-house-item">
                                <div class="detail-house-key">土地坪數</div>
                                <span>：</span>
                                <div class="detail-house-value">8.78坪</div>
                            </div>
                                            </div>
                </div>, <div class="detail-house-box">
                    <div class="detail-house-name">生活機能</div>
                    <div class="detail-house-content">
                                                    <div class="detail-house-item">
                                <i class="detail-house-2"></i>
                                <div class="detail-house-life">近便利商店</div>
                            </div>
                                                    <div class="detail-house-item">
                                <i class="detail-house-3"></i>
                                <div class="detail-house-life">近傳統市場</div>
                            </div>
                                                    <div class="detail-house-item">
                                <i class="detail-house-1"></i>
                                <div class="detail-house-life">近百貨公司</div>
                            </div>
                                                    <div class="detail-house-item">
                                <i class="detail-house-5"></i>
                                <div class="detail-house-life">近公園綠地</div>
                            </div>
                                                    <div class="detail-house-item">
                                <i class="detail-house-6"></i>
                                <div class="detail-house-life">近學校</div>
                            </div>
                                                    <div class="detail-house-item">
                                <i class="detail-house-7"></i>
                                <div class="detail-house-life">近醫療機構</div>
                            </div>
                                                    <div class="detail-house-item">
                                <i class="detail-house-4"></i>
                                <div class="detail-house-life">近夜市</div>
                            </div>
                                            </div>
                </div>, <div class="detail-house-box">
                    <div class="detail-house-name">附近交通</div>
                    <div class="detail-house-content">
                                                                                    <div class="detail-house-item">
                                    <i class="detail-house-trabus"></i>
                                    <div class="detail-house-value">澄清路公車站</div>
                                </div>
                                                            <div class="detail-house-item">
                                    <i class="detail-house-trabus"></i>
                                    <div class="detail-house-value">本館路公車站</div>
                                </div>
                                                                                                                <div class="detail-house-item">
                                    <i class="detail-house-tragoods"></i>
                                    <div class="detail-house-value">黃線捷運站</div>
                                </div>
                                                                                                                <div class="detail-house-item">
                                    <i class="detail-house-tratrain"></i>
                                    <div class="detail-house-value">鳳山火車站</div>
                                </div>
                                                            <div class="detail-house-item">
                                    <i class="detail-house-tratrain"></i>
                                    <div class="detail-house-value">高雄火車站</div>
                                </div>
                                                                        </div>
                </div>''']}
}

insert_sql ="""
            INSERT INTO `ex_main`
            (`id`, `unid`, `source`, `number`, `city`, `area`, `title`,
            `road`, `style`, `ping`, `parking`, `age`, `floor`, `type`, 
            `direction`, `fee`, `builder`, `unit`, `price`, `description`, 
            `around`, `status`, `community`, `view_num`, `add_time`, 
            `update_time`, `is_closed`) VALUES 
            """

select_sql ="SELECT `number` FROM `ex_main` WHERE `number` = %s"

for houseid,this_data in data_list.items():
    db_conn.execute(select_sql,[houseid])
    
    if db_conn.fetchone() is None:
        insert_sql += "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s),"
        
        for key,vals in this_data.items():
            print(key)

insert_sql = insert_sql.rstrip(',')    
print(insert_sql)