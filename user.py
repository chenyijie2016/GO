# -*- coding: utf-8 -*-
import json

USER_DATABASE_FILE = 'user_database/user_list.db'
USER_INFORMATION_DATABASE_FILE = 'user_database/user_info.db'


# 注意:注册前必须要有该路径和数据文件
def register(user):
    """
    用户注册
    :param user: 
    :return: true表示注册成功,false表示注册失败
    """
    user_db = open(USER_DATABASE_FILE, 'r')
    user_list = json.loads(user_db.read())

    # 检验id是否存在
    for pre_user in user_list:
        if user['user_id'] == pre_user['user_id']:
            return False

    # 直接添加进数据库
    user_list.append(user)
    user_db.close()
    user_db = open(USER_DATABASE_FILE, 'w')
    user_db.write(json.dumps(user_list))
    user_db.close()
    return True


# TODO 校验密码改用更安全的方式实现
# TODO 考虑密码用SHA256加密
def login(user):
    """
    用户登录
    :param user: 
    :return: true表示登录成功,false表示登录失败
    """
    user_db = open(USER_DATABASE_FILE, 'r')
    user_list = json.loads(user_db.read())
    user_db.close()
    # 检验id是否存在，并校验密码
    for pre_user in user_list:
        if user['user_id'] == pre_user['user_id']:
            if user['password'] == pre_user['password']:
                return True

    return False


def set_user_information(user_info):
    """
    设置用户信息
    :param user_info: 
    """
    info_db = open(USER_INFORMATION_DATABASE_FILE, 'r')
    info_list = json.loads(info_db.read())
    info_db.close()

    if check_id_in_list(user_info['user_id'], info_list):

        for info in info_list:
            if info['user_id'] == user_info['user_id']:
                info['user_id'] = user_info['user_id']
    else:

        info_list.append(user_info)

    info_db = open(USER_INFORMATION_DATABASE_FILE, 'w')
    info_db.write(json.dumps(info_list))
    info_db.close()


def get_user_information(user):
    """
    获取用户信息
    :param user: 
    :return: 
    """
    info_db = open(USER_INFORMATION_DATABASE_FILE, 'r')
    info_list = json.loads(info_db.read())
    info_db.close()

    for info in info_list:
        if info['user_id'] == user['user_id']:
            return info

    raise 'Can Not Find User In DataBase'


def modify_user_information(user_info):
    info_db = open(USER_INFORMATION_DATABASE_FILE, 'r')
    info_list = json.loads(info_db.read())
    info_db.close()

    for info in info_list:
        if info['user_id'] == user_info['user_id']:
            info['country'] = user_info['country']
            info['intr'] = user_info['intr']

    info_db = open(USER_INFORMATION_DATABASE_FILE, 'w')
    info_db.write(json.dumps(info_list))
    info_db.close()




def check_id_in_list(id, list_to_check):
    """
    检测该id是否在数据库中出现
    :param id: 
    :param list_to_check: 
    :return: 
    """
    for x in list_to_check:
        if x['user_id'] == id:
            return True

    return False
