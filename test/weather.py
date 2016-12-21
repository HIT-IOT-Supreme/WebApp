# -*- coding: utf-8 -*-
from requests import get

KEY = '5ftvygbtl1i2qilk'

HOST = 'https://api.thinkpage.cn/v3'

WHEATHER_NOW = HOST + '/weather/now.json'
WHEATHER_DAILY = HOST + '/weather/daily.json'

AIR_URL = '/air'

address = {
    'key': KEY,
    'location': 'haerbin'
}

result = get(WHEATHER_NOW, params=address)
print result.url
print result.content

result = get(WHEATHER_DAILY, params=address)
print result.url
print result.content


