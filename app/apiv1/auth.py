# -*- coding: utf-8 -*-
import json
from flask import jsonify
from flask_restful import Resource, reqparse
from . import api
from .. import db
from ..models import User, Clock

auth_parser = reqparse.RequestParser()
auth_parser.add_argument('token', type=str, required=True)

clock_parser = reqparse.RequestParser()
clock_parser.add_argument('time', type=str, required=True)


class AuthAPI(Resource):

    def get(self):

        users = User.query.all()
        return jsonify(map(eval, map(str, users)))

    def post(self):
        args = auth_parser.parse_args()
        user = User(**args)
        db.session.add(user)

        try:
            db.session.commit()
        except Exception:
            return jsonify({'code': '404'})

        return jsonify({'code': '200'})

api.add_resource(AuthAPI, '/auth/')


class ClockAPI(Resource):

    def get(self):
        user = User.query.filter_by(id=1).first()
        return jsonify(map(eval, map(str, user.clocks)))

    def post(self):
        args = clock_parser.parse_args()
        clock = Clock(time=args['time'], user_id=1)
        db.session.add(clock)

        try:
            db.session.commit()
        except Exception:
            return jsonify({'code': '404'})

        return jsonify({'code': '200'})

api.add_resource(ClockAPI, '/clock/')