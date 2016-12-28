# -*- coding: utf-8 -*-
import json
import requests
from flask import jsonify
from flask_restful import Resource
from . import api

KEY = '5ftvygbtl1i2qilk'

HOST = 'https://api.thinkpage.cn/v3'
WEATHER_NOW = HOST + '/weather/now.json'


class WeatherAPI(Resource):
    def get(self):

        return jsonify(info=parse_weather())

api.add_resource(WeatherAPI, '/weather/')


def parse_weather():
    address = {
        'key': KEY,
        'location': 'haerbin'
    }
    result = json.loads(requests.get(WEATHER_NOW, params=address).content)['results'][0]
    return u'主人～您所在的城市为' + result['location']['name'] + ',' \
            + u'当前的温度为' + result['now']['temperature'] + ',' \
            + u'天气为' + result['now']['text'] + '.' \
            + u'要注意身体噢'
