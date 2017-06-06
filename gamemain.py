#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import user
import game_function as gf
import AI

SGF_FILE_PATH = 'game_database/sgf/'


def write_record(game):
    """
    write game message to sgf file
    :param game: 
    """
    f = open(SGF_FILE_PATH + game['game_id'] + '.sgf', 'a')
    f.write(';' + game['msg'])
    f.close()


def create_sgf(item):
    """
    create empty sgf file
    :param item: 
    """
    f = open(SGF_FILE_PATH + item['game_id'] + '.sgf', 'w')
    f.write(';SZ[19]\nFF[3]\n')
    f.write('PB[' + item['player1'] + ']\n')
    f.write('PW[' + item['player2'] + ']\n')
    f.write('DT[' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ']\n')
    f.write(('EV[' + 'Game ID ' + item['game_id'] + ']\n'))
    f.close()


def register(gameuser):
    """
    user register
    :param gameuser: 
    :return: TRUE/FALSE
    """
    if user.register(gameuser):
        print('Successfully Register User:', gameuser['user_id'])
        # set defult user information
        user.set_user_information(
            {'user_id': gameuser['user_id'], 'rank': 1000, 'grade': '18k', 'country': 'unknown', 'intr': 'none',
             'win': 0, 'lose': 0})
        return True
    else:
        return False


def login(gameuser):
    """
    user login
    :param gameuser(dict) {"user_id", "password"}:
    :return: TRUE/FALSE
    """
    if user.login(gameuser):
        return True
    else:
        return False


def deal_game_start(game):
    """
    game start
    :param game: game(dict)
    :return: (dict) operate: ["create", "join", "none"] status [1 --> success, 0 --> fail]
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
    get game information
    :param game(dict): {"game_id","....", ...}
    :return: 
    """
    return gf.get_game(game)


def get_wait_game():
    return gf.get_wait_game()


def ai_game(msg):
    """
    deal with AI game message
    :param msg(dict)["game_id", "user_id", "method"]:

    property: method：
        create:create a new AI game
        play: playing
    """
    if msg['method'] == 'create':
        if gf.is_exist_game(msg):
            return {'operate': 'fail'}
        else:
            create_sgf({'game_id': msg['game_id'], 'player1': msg['user_id'], 'player2': 'MuGo'})
            AI.create_ai_game(msg)
            return {'operate': 'success'}

    if msg['method'] == 'play':
        return AI.play_ai_game(msg)


def get_user_information(user_):
    return user.get_user_information(user_)


def modify_user_information(msg):
    return user.modify_user_information(msg)


def game_over(msg):
    return gf.game_over(msg)
