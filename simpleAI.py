# -*- coding: utf-8 -*-
import argparse
import argh
import sys
import os
import gtp as gtp_lib

from policy import PolicyNetwork
from strategies import RandomPlayer, PolicyNetworkBestMovePlayer, PolicyNetworkRandomMovePlayer, MCTS
from load_data_sets import DataSet, parse_data_sets

string = 'abcdefghijklmnopqrstuvwxyz'
read_file = "D:\go\savedmodel"
data_file = "data.txt"
data_file_path = r'game_database/data/'


def AI(msg):
    global read_file
    data_file = data_file_path + msg['game_id'] + '.txt'
    # 提取信息
    x = msg['msg'][2].upper()
    y = string.index(msg['msg'][3])
    color = ''
    if msg['msg'][0] == 'B':
        color = 'W'
    else:
        color = 'B'

        # 初始化策略网络
    n = PolicyNetwork(use_cpu=True)
    instance = PolicyNetworkBestMovePlayer(n, read_file)
    gtp_engine = gtp_lib.Engine(instance)
    # sys.stderr.write("GTP Enginene ready\n")
    AI_cmd = parse_AI_instruction(color)

    # 查看是否已经开始下棋并记录
    if os.path.exists(data_file):
        rfile = open(data_file, 'r')
        cmd_list = rfile.readlines()
        for cmd in cmd_list:
            cmd = cmd.strip('\n ')
            if cmd == '':
                continue
            gtp_engine.send(cmd)
        # sys.stdout.write(cmd)
        # sys.stdout.flush()
        rfile.close()

    # 解析对方下棋指令，写进data
    wfile = open(data_file, 'a')
    player_cmd = parse_player_input(msg['msg'][0], x, y)
    wfile.write(player_cmd + '\n')
    gtp_engine.send(player_cmd)
    # sys.stdout.write(player_cmd + '\n')
    # sys.stdout.flush()

    gtp_reply = gtp_engine.send(AI_cmd)
    gtp_cmd = parse_AI_input(color, gtp_reply)
    wfile.write(gtp_cmd + '\n')
    wfile.close()
    # sys.stdout.write(gtp_reply)
    # sys.stdout.flush()

    response = color + '[' + gtp_reply[2].lower() + string[int(gtp_reply[3:])] + ']'
    # sys.stdout.write(response)
    # sys.stdout.flush()

    return {'game_id': msg['game_id'], 'msg': response}


def parse_AI_instruction(color):
    return "genmove " + color.upper()


def parse_AI_input(color, gtp_reply):
    return "play " + color.upper() + ' ' + gtp_reply[2:]


def parse_player_input(color, x, y):
    return "play " + color.upper() + ' ' + str(x).upper() + str(y)


if __name__ == "__main__":
    AI({'game_id': 123, 'msg': 'B[ab]'})
