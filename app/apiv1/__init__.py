# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api

apiv1_bp = Blueprint('apiv1', __name__)
api = Api(apiv1_bp)

from . import views, robot