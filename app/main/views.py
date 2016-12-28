# -*- coding: utf-8 -*-
from . import main_bp


@main_bp.route('/')
def index():
    return 'Oh 智障 杜老大!～'
