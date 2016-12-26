# -*- coding: utf-8 -*-
from flask import jsonify
from flask_restful import Resource
from . import api


class Control(Resource):

    def post(self):


        return jsonify({'code': '200'})

api.add_resource(Control, '/control/')