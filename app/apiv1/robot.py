# -*- coding: utf-8 -*-
import json
import requests
from flask import jsonify
from flask_restful import Resource
from . import api

KEY = '393d7387723348a79ea7cd846535eb3b'
URL = 'http://www.tuling123.com/openapi/api'


class RobotAPI(Resource):

    def get(self, info):

        data = {
            'key': KEY,
            'info': info
        }

        result = requests.post(URL, data=data)
        return jsonify(json.loads(result.content))

api.add_resource(RobotAPI, '/robot/<info>/')