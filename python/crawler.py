import requests
import json
from bs4 import BeautifulSoup

url = 'https://sale.591.com.tw/home/search/list?type=2&&shType=list&regionid=17&firstRow=0&totalRows=14679&timestamp=1548122419382'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
response = requests.get(url, headers=headers)
#soup = BeautifulSoup(response.text,'html.parser')

json_text = response.text
json_text = json_text.encode("utf8").decode("cp950", "ignore")
data = json.loads(json_text)

house_list = data['data']['house_list']

for house in house_list:
	print(house['title'])
	print('總價 : ' + str(house['price']) )
	print('格局 : ' + str(house['room']) )
	print('樓層 : ' + house.get('floor', '') )
	print('地址 : ' + house.get('address', '') )
	has_carport = house.get('has_carport', 0)
	has_carport_text = '是' if int(has_carport) == 1 else '否'
	print('車位 : ' + has_carport_text)
	print('單價' + house.get('unit_price', ''))
	print('單價' + house.get('show_unitprice', '')+house.get('show_unitprice_unit', ''))
	print('--------------------------')