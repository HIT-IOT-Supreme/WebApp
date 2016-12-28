# -*- coding: utf-8 -*-
from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(64), unique=True)

    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return str({
            'token': self.token
        })


class Clock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Time)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User',
                backref=db.backref('clocks', lazy='dynamic'))

    def __init__(self, time, user_id):

        user = User.query.filter_by(id=user_id).first()
        self.user = user
        self.time = time

    def __repr__(self):
        return str({
            'time': str(self.time)
        })


class Sleep(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User',
                backref=db.backref('sleeps', lazy='dynamic'))

    def __init__(self, start_time, end_time, user_id):

        user = User.query.filter_by(id=user_id).first()
        self.user = user
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return str({
            'start_time': str(self.start_time),
            'end_time': str(self.end_time)
        })


# 暂无各种Sensor的数据存储需求
# class Sensor(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     time = db.Column(db.DateTime)
#     data = db.Column(db.Float)
#
#     def __init__(self, data, time):
#         self.data = data
#         self.time = time
