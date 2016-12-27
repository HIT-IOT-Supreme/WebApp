# -*- coding: utf-8 -*-
from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(64), unique=True)
    clocks = db.relationship('Clock', backref=db.backref('user', lazy='dynamic'),
                             lazy='dynamic')

    def __init__(self, token):
        self.token = token


class Clock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    time = db.Column(db.DateTime)

    def __init__(self, user_id, time):
        self.user_id = user_id
        self.time = time


class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    data = db.Column(db.Float)

    def __init__(self, data, time):
        self.data = data
        self.time = time