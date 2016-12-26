# -*- coding: utf-8 -*-
from flask import Flask
import flask_restful as restful
#from flask import json
import json
import requests
from flask import jsonify
from flask_restful import Resource

KEY = '5ftvygbtl1i2qilk'

HOST = 'https://api.thinkpage.cn/v3'

app = Flask(__name__)
api = restful.Api(app)


WHEATHER_NOW = HOST + '/weather/now.json'  #get
WHEATHER_ALARM = HOST + '/weather/alarm.json'
AIR_NOW = HOST + '/air/now.json'
LIFE_SUGGESTION = HOST + '/life/suggestion.json'  #get
LIFE_CHINESE_CALENDAR = HOST + '/life/chinese_calendar.json'
GEO_SUN = HOST + '/geo/sun.json'

#keywords:now,suggestion,air,alarm,sun,calendar
request = {"now": WHEATHER_NOW, "suggestion": LIFE_SUGGESTION,
           "air": AIR_NOW, "alarm": WHEATHER_ALARM,
           "sun": GEO_SUN, "calendar": LIFE_CHINESE_CALENDAR}

class getWeather(Resource):
    def get(self,info):
        address = {
            'key': KEY,
            'location': 'haerbin'
        }
        req = request[info]
        result_now_weather = requests.get(req, params=address)
        return jsonify(json.loads(result_now_weather.content,encoding='utf-8'))

api.add_resource(getWeather, '/weathers/<string:info>')

if __name__ == '__main__':
    app.run(port= 8880,debug=True)