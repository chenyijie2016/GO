#!/usr/bin/env python
# -*- coding: utf-8 -*-
import user
import os
import game_function

# filelist = [x for x in os.listdir('game_database/log') if os.path.isfile(x)]
#
# print(filelist)
# print(os.listdir('game_database/log'))
# print(os.path())
#
# user1 = {'user_id': 'bot1', 'password': '123456'}
#
# user2 = {'user_id': 'bot2', 'password': '456456'}
#
# user3 = {'user_id': 'bot2', 'password': '45646'}
#
# if user.register(user1):
#     print('注册成功')
# else:
#     print('注册失败')
#
#
# if user.register(user2):
#     print('注册成功')
# else:
#     print('注册失败')
#
#
# if user.login(user3):
#     print('登录成功')
# else:
#     print('登录失败')

i = {'game_id': '2', 'user_id': 'test'}
j = {'game_id': '2', 'user_id': 'bot'}

# game.create_game(i)
game_function.create_game(i)

print(game_function.is_exist_game(i))

print(game_function.can_join_game(i))

game_function.join_game(j)
