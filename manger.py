#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/16 21:05
# @Author  : cyj
# @Site    : 
# @File    : manger.py.py
# @Software: PyCharm Community Edition
import json

USER_DATABASE_FILE = 'user_database/user_list.db'
DATABASE_FILE = 'game_database/game_status.db'


def main():
    print('输入选项进行操作:')
    print('[1]:清空所有数据')
    print('[2]:显示已注册用户')
    print('[3]:显示对局信息')
    option = input()
    if option == '1':
        clear_all()
    if option == '2':
        showDataBase()
    if option == '3':
        showGameDataBase()
    print('-----------------')
    main()


def clear_all():
    a = input('确定要清除所有数据？(Y/N)')
    if a == 'y' or a == 'Y':
        f = open(USER_DATABASE_FILE, 'w')
        f.write('[]')
        f.close()
        f = open(DATABASE_FILE, 'w')
        f.write('[]')
        f.close()
        print('清除数据库成功')


def showDataBase():
    f = open(USER_DATABASE_FILE, 'r')
    user_list = json.loads(f.read())
    if len(user_list) == 0:
        print('没有用户信息')
        return
    for user in user_list:
        print('用户名: ', user['user_id'], ' 密码: ******')


def showGameDataBase():
    f = open(DATABASE_FILE, 'r')
    game_list = json.loads(f.read())
    if len(game_list) == 0:
        print('没有对局信息')
        return
    for game in game_list:
        print('对局ID: ', game['game_id'], end=' ')
        print('创建者: ', game['player1'], end=' ')
        print('游戏人数: ', game['player_num'])


if __name__ == '__main__':
    main()
