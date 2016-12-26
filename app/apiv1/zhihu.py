# -*- coding: utf-8 -*-
import json
import requests
from flask import jsonify
from flask_restful import Resource
from . import api

URL = 'http://news-at.zhihu.com/api/4/news/latest'


class ZhiHu(Resource):

    def get(self):

        # 知乎后台对user-agent进行限制，必须模拟为真实浏览器才可访问
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
        }

        result = requests.get(URL, headers=headers)
        return jsonify(json.loads(result.content))

api.add_resource(ZhiHu, '/zhihu/')