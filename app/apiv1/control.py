# -*- coding: utf-8 -*-
from flask import jsonify
from flask_restful import Resource
from . import api


class Control(Resource):

    def get(self, action):

        if action == '':
            pass

        return jsonify({'action': action})

api.add_resource(Control, '/control/<action>/')