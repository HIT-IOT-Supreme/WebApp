# -*- coding: utf-8 -*-
from . import main_bp


@main_bp.route('/')
def index():
    return 'Hello World!'
