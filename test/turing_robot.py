# -*- coding: utf-8 -*-
from requests import post

KEY = '393d7387723348a79ea7cd846535eb3b'

URL = 'http://www.tuling123.com/openapi/api'

data = {
    'key': KEY,
    'info': u'告诉我最近有什么新闻'
}

result = post(URL, data=data)

print result.content

data = {
    'key': KEY,
    'info': u'从哈尔滨到汝州的火车票'
}

result = post(URL, data=data)

print result.content