# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit

import gamemain

app = Flask(__name__, template_folder='./')
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)

# 设置是否输出调试信息
DEBUG = True


@app.route('/')
def index():
    if DEBUG:
        print('访问')
    # 返回网站主页
    return render_template('static/go.html')


@app.route('/register')
def register_html():
    if DEBUG:
        print('注册')
    return render_template('static/register.html')


@app.route('/login')
def login_html():
    if DEBUG:
        print('登录')
    return render_template('static/login.html')


@app.route('/information')
def information():
    if DEBUG:
        pass
    return render_template('static/information.html')


# 以下是接受到各个不同事件时的处理函数

# 测试遗留 忽略即可
@socketio.on('client_event')
def client_msg(msg):
    # print('接受消息:', end='')
    # print(msg)
    # res = go.place(msg['data'])
    # emit('server_response', {'data': res})
    # emit('server_response', {'data': msg['data']})
    pass


# 建立连接
@socketio.on('connect_event')
def connected_msg(msg):
    if DEBUG:
        print('连接')
    emit('server_response', {'data': msg['data']})


@socketio.on('game_start')
def game_start_msg(msg):
    """
    游戏开始事件
    :param msg: 
    """
    if DEBUG:
        print('接受到游戏创建/加入请求:', msg)

    result = gamemain.deal_game_start(msg)

    if result['operate'] == 'create':
        emit('game_start', {'game_id': msg['game_id'], 'user_id': msg['user_id'], 'begin': '0', 'side': 'black'},
             broadcast=True)
        if DEBUG:
            print('创建游戏成功')

    if result['operate'] == 'join':
        emit('game_start', {'user_id': msg['user_id'], 'game_id': msg['game_id'], 'begin': '1', 'side': 'white',
                            'emeny': gamemain.get_game(msg)['player1']}, broadcast=True)
        if DEBUG:
            print('加入游戏成功')

    if result['operate'] == 'none':
        emit('start_error', {'game_id': msg['game_id']})
        if DEBUG:
            print('加入游戏失败')


@socketio.on('play_game_server')
def play_game_msg(msg):
    """
    接受游戏落字消息
    :param msg: 
    """
    if DEBUG:
        print('落子信息:', msg)
    # 记录到sgf文件中
    gamemain.write_record(msg)
    # 向其他连接的客户端广播
    emit('play_game_client', msg, broadcast=True)


@socketio.on('message')
def message(msg):
    """
    处理用户发来的消息
    直接向其他客户端广播
    :param msg: 
    """
    if DEBUG:
        print('用户聊天信息:', msg)
    emit('message', msg, broadcast=True)


@socketio.on('get_wait_game')
def send_wait_game(msg):
    if DEBUG:
        print('发送处于等待状态的游戏列表')
    emit('game_info', {'data': gamemain.get_wait_game()})


@socketio.on('register')
def register(msg):
    """
    处理注册
    :param msg: 
    """
    if DEBUG:
        print('收到注册请求', msg)
    if gamemain.register(msg):
        emit('register_reply', {'data': 'success'})
        if DEBUG:
            print('注册成功')
    else:
        emit('register_reply', {'data': 'failed'})
        if DEBUG:
            print('注册失败')


@socketio.on('login')
def login(msg):
    """
    处理登录
    :param msg: 
    """
    if DEBUG:
        print('收到登录请求', msg)

    if gamemain.login(msg):
        emit('login_reply', {'data': 'success'})
        if DEBUG:
            print('登录成功')

    else:
        emit('login_reply', {'data': 'failed'})
        if DEBUG:
            print('登录失败')


@socketio.on('AI_event')
def AI_message(msg):
    if msg['method'] == 'create':
        pass


@socketio.on('user_information')
def send_information(msg):
    if DEBUG:
        print('获取用户信息')
    emit('user_information', gamemain.get_user_information(msg))


@socketio.on('set_user_information')
def modify_information(msg):
    if DEBUG:
        print('修改用户信息', msg)

    gamemain.modify_user_information(msg)
    emit('set_user_information_reply_ok', {})


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080)
