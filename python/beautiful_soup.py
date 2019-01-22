import requests
import json
from bs4 import BeautifulSoup

url = 'https://sale.591.com.tw/home/search/list?type=2&&shType=list&regionid=17&firstRow=0&totalRows=14679&timestamp=1548122419382'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
response = requests.get(url, headers=headers)

json_text = response.text
json_text = json_text.encode("utf8").decode("cp950", "ignore")
data = json.loads(json_text)

house_list = data['data']['house_list']

for house in house_list:
    houseid = house['houseid']
    
    url = 'https://sale.591.com.tw/home/house/detail/2/{}.html'.format(houseid)

    content_res = requests.get(url, headers=headers)
    
    content_text = content_res.text
    
    soup = BeautifulSoup(content_text, 'html.parser')
    soup.prettify()
    
    # 圖片
    photo_tag = soup.find_all('div', id='img_list')
    for tag in photo_tag:
        tdTags = tag.find_all("img")
        for tag in tdTags:
            print(tag.get('src'))  
        
    # 朝向
    '''
    addr_tag = soup.find_all('div', class_='info-addr-content')
    for one in addr_tag:      
        key_vals = one.find_all('span',class_='info-addr-key')              
        for key in key_vals:
            if key.get_text() == '朝向':
                this_vals = key.find_next_siblings('span')
                print(this_vals[0].text)
    '''
