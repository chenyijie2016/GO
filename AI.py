# -*- coding: utf-8 -*-
class AI(object):
    def __init__(self, game_message):
        self.game_id = game_message['game_id']
        self.game_record = self.load_game_record()

    def load_game_record(self):
        """
        加载游戏记录
        :return: 
        """
        return self.game_record

    def reply(self):
        """
        返回AI决策
        :return: 
        """
        return
