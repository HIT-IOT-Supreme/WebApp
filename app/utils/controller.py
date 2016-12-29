# -*- coding: utf-8 -*-
import os
import thread


def break_up():
    thread.start_new_thread(shell_break_up, ())


def play_music():
    pass
    # thread.start_new_thread(shell_play_music, ())


def shell_break_up():
    os.system('sudo python scripts/sunRaise.py')


def shell_play_music():
    os.system('mpg123 static/demo.mp3')