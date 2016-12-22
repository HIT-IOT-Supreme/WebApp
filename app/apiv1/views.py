# -*- coding: utf-8 -*-
from flask import jsonify
from flask_restful import Resource
from . import api


class HelloWorld(Resource):

    def get(self):
        result = {
            'info': 'Hello sb dusz!'
        }
        return jsonify(result)

api.add_resource(HelloWorld, '/')