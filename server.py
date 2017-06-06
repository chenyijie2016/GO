# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit

import gamemain

app = Flask(__name__, template_folder='./')
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)

# TO print Debug information?
DEBUG = True


# main page
@app.route('/')
def index():
    if DEBUG:
        print('connect')
    return render_template('static/go.html')


@app.route('/register')
def register_html():
    if DEBUG:
        print('register')
    return render_template('static/register.html')


@app.route('/login')
def login_html():
    if DEBUG:
        print('login')
    return render_template('static/login.html')


@app.route('/information')
def information():
    if DEBUG:
        pass
    return render_template('static/information.html')


@app.route('/blockchain', methods=['POST'])
def post_info():
    print(request.form.get('hello'))
    return 'ok'


# just ignore it
@socketio.on('client_event')
def client_msg(msg):
    # print(msg)
    # res = go.place(msg['data'])
    # emit('server_response', {'data': res})
    # emit('server_response', {'data': msg['data']})
    pass


# establish connection with client
# in test mod
@socketio.on('connect_event')
def connected_msg(msg):
    if DEBUG:
        print('**')
    emit('server_response', {'data': msg['data']})


@socketio.on('game_start')
def game_start_msg(msg):
    """
    deal with game start message
    :param msg: 
    """
    if DEBUG:
        print('request for game start', msg)

    result = gamemain.deal_game_start(msg)

    if result['operate'] == 'create':
        emit('game_start', {'game_id': msg['game_id'], 'user_id': msg['user_id'], 'begin': '0', 'side': 'black'},
             broadcast=True)
        if DEBUG:
            print('create game OK')

    if result['operate'] == 'join':
        emit('game_start', {'user_id': msg['user_id'], 'game_id': msg['game_id'], 'begin': '1', 'side': 'white',
                            'emeny': gamemain.get_game(msg)['player1']}, broadcast=True)
        if DEBUG:
            print('join game OK')

    if result['operate'] == 'none':
        emit('start_error', {'game_id': msg['game_id']})
        if DEBUG:
            print('join game ERROR')


@socketio.on('play_game_server')
def play_game_msg(msg):
    """
    play !
    :param msg: 
    """
    if DEBUG:
        print('play info:', msg)
    # write log to sgf file
    gamemain.write_record(msg)
    # broadcast to other client
    emit('play_game_client', msg, broadcast=True)


@socketio.on('message')
def message(msg):
    """
    user mssage
    broadcast to other client
    :param msg: 
    """
    if DEBUG:
        print('message:', msg)
    emit('message', msg, broadcast=True)


@socketio.on('get_wait_game')
def send_wait_game(msg):
    if DEBUG:
        print('sending waiting game')
    emit('game_info', {'data': gamemain.get_wait_game()})


@socketio.on('register')
def register(msg):
    if DEBUG:
        print('request for register', msg)
    if gamemain.register(msg):
        emit('register_reply', {'data': 'success'})
        if DEBUG:
            print('register OK')
    else:
        emit('register_reply', {'data': 'failed'})
        if DEBUG:
            print('register ERROR')


@socketio.on('login')
def login(msg):
    if DEBUG:
        print('request for login', msg)

    if gamemain.login(msg):
        emit('login_reply', {'data': 'success'})
        if DEBUG:
            print('login OK')

    else:
        emit('login_reply', {'data': 'failed'})
        if DEBUG:
            print('login ERROR')


@socketio.on('AI_event')
def AI_message(msg):

    if DEBUG:
        print('receive AI message', msg)
    result = gamemain.ai_game(msg)
    if msg['method'] == 'create':
        if result['operate'] == 'success':
            emit('ai_game_start', {})
        else:
            emit('start_error', msg)

    if msg['method'] == 'play':
        if DEBUG:
            print('sending AI message', result)
        emit('ai_game_client', result)


@socketio.on('user_information')
def send_information(msg):
    if DEBUG:
        print('get user information')
    emit('user_information', gamemain.get_user_information(msg))


@socketio.on('set_user_information')
def modify_information(msg):
    if DEBUG:
        print('set user information', msg)

    gamemain.modify_user_information(msg)
    emit('set_user_information_reply_ok', {})


@socketio.on('game_over_event')
def game_over(msg):
    if DEBUG:
        print('game over message', msg)
    emit('game_over', msg, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080)
