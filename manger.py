#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/16 21:05
# @Author  : cyj
# @Site    : 
# @File    : manger.py.py
# @Software: PyCharm Community Edition
import json
import os

USER_DATABASE_FILE = 'user_database/user_list.db'
DATABASE_FILE = 'game_database/game_status.db'
USER_INFO_DATABASE = 'user_database/user_info.db'

def main():
    print('Enter the options:')
    print('[1]:Clear all data')
    print('[2]:Show registered users')
    print('[3]:Show all game information')
    print('[4]:Clear all game information')
    option = input()
    if option == '1':
        clear_all()
    if option == '2':
        showDataBase()
    if option == '3':
        showGameDataBase()
    if option =='4':
        clearGameStatus()

    print('-----------------')
    main()


def clear_all():
    a = input('Are you sure you want to clear all data?(Y/N)')
    if a == 'y' or a == 'Y':
        f = open(USER_DATABASE_FILE, 'w')
        f.write('[]')
        f.close()
        f = open(DATABASE_FILE, 'w')
        f.write('[]')
        f.close()
        f = open(USER_INFO_DATABASE, 'w')
        f.write('[]')
        f.close()
        os.system('del game_database\sgf\*.sgf')
        print('Clear the database successfully!')


def showDataBase():
    f = open(USER_DATABASE_FILE, 'r')
    user_list = json.loads(f.read())
    if len(user_list) == 0:
        print('No user information')
        return
    for user in user_list:
        print('User ID: ', user['user_id'], ' Password: ******')


def showGameDataBase():
    f = open(DATABASE_FILE, 'r')
    game_list = json.loads(f.read())
    if len(game_list) == 0:
        print('No information on the game')
        return
    for game in game_list:
        print('Game ID: ', game['game_id'], end=' ')
        print('Creater: ', game['player1'], end=' ')
        print('Player Number: ', game['player_num'])


def clearGameStatus():
    f = open(DATABASE_FILE, 'w')
    f.write('[]')
    f.close()
    print('Clear the database successfully!')

if __name__ == '__main__':
    main()
