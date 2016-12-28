# -*- coding: utf-8 -*-
from requests import post

URL = 'http://localhost:5000/api/clock/'

data = {
    'time': '00:00:00'
}

result = post(URL, data=data)
print result