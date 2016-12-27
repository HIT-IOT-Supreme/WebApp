# -*- coding: utf-8 -*-
import base64
import json
from requests import post, get

APP_KEY = 'a49b555506bfc2cee73b95cf'
MASTER_SECRET = 'c9fe577440420acc429b74dc'

HOST = 'https://api.jpush.cn/v3/push'

headers = {
    'Authorization': 'Basic ' + base64.b64encode(APP_KEY+':'+MASTER_SECRET)
}

data = json.loads(get('http://localhost:5000/api/zhihu').content)


jpush_data = {
    'platform': ['android'],
    'audience': 'all',
    'message': {
        'msg_content': data,
        'content_type': 'test'
    }
}

print jpush_data
result = post(HOST, headers=headers, json=jpush_data)
print result.content


