#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/7 14:05
# @Author  : cyj
# @Site    : 
# @File    : server.py
# @Software: PyCharm
'''
The server of the basic database, using network to inquire data.
'''

from flask import Flask, render_template, session, request

app = Flask(__name__, template_folder='./')
app.config['SECRET_KEY'] = 'secret!'


@app.route('/', methods=['POST'])
def get_data():
    get_func = {
        'user': get_user_data,
        'game': get_game_data,
        'ai': get_ai_data
    }
    set_func = {

    }
    target_data_mode = request.form.get('mode')
    target_data_type = request.form.get('type')
    target_data_descri = request.form.get('game_id')
    if target_data_mode == 'get':
        return get_func[target_data_type](target_data_descri)
    elif target_data_mode == 'set':
        return set_func[target_data_type](target_data_descri)


def get_user_data():
    pass


def get_game_data():
    pass


def get_ai_data():
    pass


if __name__ == '__main__':
    # listen all requests form port 7000
    app.run('0.0.0.0', port=7000)
