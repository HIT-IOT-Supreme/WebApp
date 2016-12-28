# -*- coding: utf-8 -*-
from flask import jsonify
from flask_restful import Resource
from . import api
from .. import timer


class Control(Resource):

    def get(self, action):

        if action == 'speech_end':
            timer.read_on()
        elif action == 'close_all':
            pass

        return jsonify({'action': action})

api.add_resource(Control, '/control/<action>/')