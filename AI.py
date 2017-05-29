# -*- coding: utf-8 -*-
import simpleAI
import json
DATABASE_FILE = 'game_database/game_status.db'
SGF_FILE_PATH = 'game_database/sgf/'


def create_ai_game(msg):
    """
    创建AI对局
    :param msg: 
    """
    game_list = load_database_to_list(DATABASE_FILE)

    newgame = {'game_id': msg['game_id'], 'player1': msg['user_id'], 'player2': 'MuGo', 'player_num': 2,
               'status': 'fight'}

    game_list.append(newgame)

    write_list_to_database(game_list, DATABASE_FILE)


def play_ai_game(msg):
    write_record(msg)
    write_record(simpleAI.AI(msg))
    return {'game_id': msg['game_id'], 'msg': simpleAI.AI(msg)['msg'], 'user_id': 'MuGo'}


def write_record(game):
    """
    记录落子信息到sgf文件中
    :param game: 
    """
    f = open(SGF_FILE_PATH + str(game['game_id']) + '.sgf', 'a')
    f.write(';' + game['msg'])
    f.close()


def load_database_to_list(DATABASE):
    """
    从数据库文件中加载list
    :param DATABASE: 
    :return: 
    """
    f = open(DATABASE, 'r')
    list_ = json.loads(f.read())
    f.close()
    return list_


def write_list_to_database(LIST, DATABASE):
    """
    将list写入数据库文件
    :param LIST: 
    :param DATABASE: 
    """
    f = open(DATABASE, 'w')
    f.write(json.dumps(LIST))
    f.close()
