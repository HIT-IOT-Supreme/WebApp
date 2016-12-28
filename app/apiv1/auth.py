# -*- coding: utf-8 -*-
from flask import jsonify
from flask_restful import Resource, reqparse
from . import api
from .. import db, timer
from ..models import User, Clock, Sleep

auth_parser = reqparse.RequestParser()
auth_parser.add_argument('token', type=str, required=True)

clock_parser = reqparse.RequestParser()
clock_parser.add_argument('time', type=str, required=True)

sleep_parser = reqparse.RequestParser()
sleep_parser.add_argument('start_time', type=str, required=True)
sleep_parser.add_argument('end_time', type=str, required=True)


class AuthAPI(Resource):

    def get(self):

        return jsonify(get_users())

    def post(self):

        try:
            add_user()
        except Exception:
            return jsonify({'code': '404'})

        return jsonify({'code': '200'})

api.add_resource(AuthAPI, '/auth/')


class ClockAPI(Resource):

    def get(self):
        return jsonify(get_clocks())

    def post(self):

        try:
            add_clock()
        except Exception:
            return jsonify({'code': '404'})

        return jsonify({'code': '200'})

api.add_resource(ClockAPI, '/clock/')


class SleepAPI(Resource):

    def get(self):
        return jsonify(get_sleeps())

    def post(self):

        try:
            add_sleep()
        except Exception:
            return jsonify({'code': '404'})

        return jsonify({'code': '200'})

api.add_resource(SleepAPI, '/sleep/')


def get_users():
    users = User.query.all()
    return map(eval, map(str, users))


def add_user():
    args = auth_parser.parse_args()
    user = User(**args)
    db.session.add(user)
    db.session.commit()


def get_clocks():
    user = User.query.filter_by(id=1).first()
    return map(eval, map(str, user.clocks))


def add_clock():
    args = clock_parser.parse_args()
    clock = Clock(time=args['time'], user_id=1)

    timer.add_timer(args['time'])

    db.session.add(clock)
    db.session.commit()


def get_sleeps():
    user = User.query.filter_by(id=1).first()
    return map(eval, map(str, user.sleeps))


def add_sleep():
    args = sleep_parser.parse_args()
    sleep = Sleep(start_time=args['start_time'], end_time=args['end_time'], user_id=1)

    db.session.add(sleep)
    db.session.commit()