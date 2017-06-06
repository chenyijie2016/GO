#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json

DATABASE_FILE = 'game_database/game_status.db'
SGF_FILE_PATH = 'game_database/sgf/'


def is_exist_game(game):
    """
    Does the game exists
    :param game: game(dict)
    :return: TRUE / FALSE 
    """

    game_list = load_database_to_list(DATABASE_FILE)

    for cur_game in game_list:
        if game['game_id'] == cur_game['game_id']:
            return True

    return False


def can_join_game(game):
    """
    can user join a existed game
    :param game: game(dict)
    :return: TRUE / FALSE 
    """
    game_list = load_database_to_list(DATABASE_FILE)

    for cur_game in game_list:
        if game['game_id'] == cur_game['game_id']:
            if cur_game['player_num'] == 1 and cur_game['status'] == 'wait':
                return True

    return False


def create_game(game):
    """
    :param game: game(dict)
    """
    game_list = load_database_to_list(DATABASE_FILE)

    new_game = {'game_id': game['game_id'], 'player1': game['user_id'], 'player_num': 1, 'status': 'wait'}
    game_list.append(new_game)

    write_list_to_database(game_list, DATABASE_FILE)


def join_game(game):
    """
    to join a existed game
    :param game: game(dict)
    """
    game_list = load_database_to_list(DATABASE_FILE)

    update_game = ''
    cur_game = ''
    for cur_game in game_list:
        if cur_game['game_id'] == game['game_id']:
            update_game = cur_game
            update_game['player_num'] = 2
            update_game['status'] = 'fight'
            update_game['player2'] = game['user_id']
            break

    game_list[game_list.index(cur_game)] = update_game

    write_list_to_database(game_list, DATABASE_FILE)


def get_game(game):
    """
    get game information with target game_id
    :param game: game(dict)
    :return: (dict)
    """
    game_list = load_database_to_list(DATABASE_FILE)

    for cur_game in game_list:
        if cur_game['game_id'] == game['game_id']:
            return cur_game


def get_wait_game():
    """
    get the waitling games list
    :return: (str)(HTML form)
    """
    game_list = load_database_to_list(DATABASE_FILE)

    wait_game_list = []

    for cur_game in game_list:
        if cur_game['status'] == 'wait':
            wait_game_list.append(cur_game)
            break
    result = ''
    for x in wait_game_list:
        result += 'Crteter ID: ' + x['player1'] + ' Game ID: ' + x['game_id'] + '<br>'
    return result


def game_over(msg):
    change_game_status(msg, 'over')


def change_game_status(game_dict, status):
    """
    change game status , called when game is over
    :param game_dict(dict):
    :param status('wait'/'fight'/'over'):
    """
    game_list = load_database_to_list(DATABASE_FILE)
    for cur_game in game_list:
        if cur_game['game_id'] == game_dict['game_id']:
            update_game = cur_game
            update_game['status'] = status
            game_list[game_list.index(cur_game)] = update_game
            break


def load_database_to_list(DATABASE):
    """
    load list from database file
    :param (constant)DATABASE: Filename
    :return: (list)
    """
    f = open(DATABASE, 'r')
    list_ = json.loads(f.read())
    f.close()
    return list_


def write_list_to_database(LIST, DATABASE):
    """
    write list to database file
    :param LIST: (list)
    :param (constant)DATABASE: Filename
    """
    f = open(DATABASE, 'w')
    f.write(json.dumps(LIST))
    f.close()
