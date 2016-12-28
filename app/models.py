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


# 暂无各种Sensor的数据存储需求
# class Sensor(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     time = db.Column(db.DateTime)
#     data = db.Column(db.Float)
#
#     def __init__(self, data, time):
#         self.data = data
#         self.time = time
