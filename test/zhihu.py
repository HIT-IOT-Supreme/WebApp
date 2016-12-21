# -*- coding: utf-8 -*-
from requests import get

NEWS = 'http://news-at.zhihu.com/api/4/news/latest'

# 知乎后台对user-agent进行限制，必须模拟为真实浏览器才可访问
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
}

result = get(NEWS, headers=headers)

print result.headers
print result.content