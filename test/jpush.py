# -*- coding: utf-8 -*-
import base64
from requests import post

APP_KEY = 'a49b555506bfc2cee73b95cf'
MASTER_SECRET = 'c9fe577440420acc429b74dc'

HOST = 'https://api.jpush.cn/v3/push'

headers = {
    'Authorization': 'Basic ' + base64.b64encode(APP_KEY+':'+MASTER_SECRET)
}

data = {
    'platform': ['android'],
    'audience': 'all',
    'message': {
        'msg_content':{
            '测试': '智障杜圣哲'
        },
        'content_type': 'test'
    }
}

result = post(HOST, headers=headers, json=data)
print result.request.headers
print result.content


