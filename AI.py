#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import simpleAI
import requests
import json

DATABASE_FILE = 'game_database/game_status.db'
SGF_FILE_PATH = 'game_database/sgf/'


def create_ai_game(msg):
    """
    create AI game
    :param msg(dict):
    """
    game_list = load_database_to_list(DATABASE_FILE)

    newgame = {'game_id': msg['game_id'], 'player1': msg['user_id'], 'player2': 'MuGo', 'player_num': 2,
               'status': 'fight'}

    game_list.append(newgame)

    write_list_to_database(game_list, DATABASE_FILE)


def play_ai_game(msg):
    write_record(msg)
    response = requests.post('http://localhost:6000', data=msg)
    # send data to localhost:6000, need to be changed?
    # print(response.content.decode('utf-8'))
    print(response.content)
    print()
    result = json.loads(response.content.decode('utf-8'))

    # result = simpleAI.AI(msg)
    write_record(result)
    return {'game_id': msg['game_id'], 'msg': result['msg'], 'user_id': 'MuGo'}


def write_record(game):
    """
    write log to sgf file
    :param game: 
    """
    f = open(SGF_FILE_PATH + str(game['game_id']) + '.sgf', 'a')
    f.write(';' + game['msg'])
    f.close()


def load_database_to_list(DATABASE):
    f = open(DATABASE, 'r')
    list_ = json.loads(f.read())
    f.close()
    return list_


def write_list_to_database(LIST, DATABASE):
    f = open(DATABASE, 'w')
    f.write(json.dumps(LIST))
    f.close()
