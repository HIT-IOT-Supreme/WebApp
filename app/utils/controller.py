# -*- coding: utf-8 -*-
import os


def break_up():
    os.system('sudo python scripts/warn.py')


def play_music():
    os.system('mpg123 static/demo.mp3')

play_music()