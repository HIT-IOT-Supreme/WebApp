# -*- coding: utf-8 -*-
import base64
import json
from requests import post, get


def _push_data(data):

    APP_KEY = 'a49b555506bfc2cee73b95cf'
    MASTER_SECRET = 'c9fe577440420acc429b74dc'

    HOST = 'https://api.jpush.cn/v3/push'

    headers = {
        'Authorization': 'Basic ' + base64.b64encode(APP_KEY + ':' + MASTER_SECRET)
    }

    jpush_data = {
        'platform': ['android'],
        'audience': 'all',
        'message': {
            'msg_content': data,
            'content_type': 'test'
        }
    }

    post(HOST, headers=headers, json=jpush_data)


def push_zhihu():
    data = json.loads(get('http://localhost:5000/api/zhihu').content)
    _push_data(data)


def push_weather():
    data = json.loads(get('http://localhost:5000/api/weather').content)
    _push_data(data)

