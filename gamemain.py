#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import user
import game_function as gf

SGF_FILE_PATH = 'game_database/sgf/'


def write_record(game):
    """
    记录落子信息到sgf文件中
    :param game: 
    """
    f = open(SGF_FILE_PATH + game['game_id'] + '.sgf', 'a')
    f.write(';' + game['msg'])
    f.close()


def create_sgf(item):
    """
    创建初始sgf文件
    :param item: 
    """
    f = open(SGF_FILE_PATH + item['game_id'] + '.sgf', 'w')
    f.write(';SZ[19]\nFF[3]\n')
    f.write('PB[' + item['player1'] + ']\n')
    f.write('PW[' + item['player2'] + ']\n')
    f.write('DT[' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ']\n')
    f.write('EV[' + '棋局ID ' + item['game_id'] + ']\n')
    f.close()


def register(gameuser):
    """
    用户注册
    :param gameuser: 
    :return: TRUE/FALSE
    """
    if user.register(gameuser):
        print('成功注册用户:', gameuser['user_id'])
        # 设置默认的用户信息
        user.set_user_information(
            {'user_id': gameuser['user_id'], 'rank': 1000, 'grade': '18k', 'country': 'unknown', 'intr': 'none',
             'win': 0, 'lose': 0})
        return True
    else:
        return False


def login(gameuser):
    """
    用户登录
    :param gameuser: 
    :return: TRUE/FALSE
    """
    if user.login(gameuser):
        return True
    else:
        return False


def deal_game_start(game):
    """
    处理开始游戏的信息
    :param game: game结构体
    :return: dict类型 operate表示操作 status 表示成功或失败
    """
    if not gf.is_exist_game(game):
        gf.create_game(game)
        return {'operate': 'create', 'status': 1}
    else:
        if gf.can_join_game(game):
            gf.join_game(game)
            create_sgf(get_game(game))
            return {'operate': 'join', 'status': 1}
        else:
            return {'operate': 'none', 'status': 0}


def get_game(game):
    """
    获取游戏信息
    :param game: 
    :return: 
    """
    return gf.get_game(game)


def get_wait_game():
    """
    获取正在等待中的游戏列表
    :return: 
    """
    return gf.get_wait_game()


def get_user_information(user_):
    return user.get_user_information(user_)


def modify_user_information(msg):
    return user.modify_user_information(msg)
