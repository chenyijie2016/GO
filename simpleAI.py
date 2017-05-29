#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/29 9:52
# @Author  : cyj
# @Site    : 
# @File    : simpleAI.py
# @Software: PyCharm Community Edition
string = 'abcdefghijklmnopqrstuvwxyz'




def AI(msg):
    x = string.index(msg['msg'][2])
    y = string.index(msg['msg'][3])

    response = ''

    if msg['msg'] == 'B':
        response += 'W'
    else:
        response += 'B'

    response += '[' + string[18 - x] + string[18 - y] + ']'

    return {'game_id': msg['game_id'], 'msg': response}
