import json

USER_DATABASE_FILE = 'user_database/user_list.db'


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
