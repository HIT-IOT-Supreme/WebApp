# -*- coding: utf-8 -*-


class Config(object):
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = 'mysql://root:0122@localhost/web_api'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True