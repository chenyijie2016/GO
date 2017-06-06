#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

USER_DATABASE_FILE = 'user_database/user_list.db'
USER_INFORMATION_DATABASE_FILE = 'user_database/user_info.db'


# Note: You must have this path and data file before registering
def register(user):
    """
    User registration
    :param user: (dict)["user_id","password"]
    :return: true/false
    """
    user_db = open(USER_DATABASE_FILE, 'r')
    user_list = json.loads(user_db.read())

    # Whether the user_id exists?
    for pre_user in user_list:
        if user['user_id'] == pre_user['user_id']:
            return False

    # Add directly to the database
    user_list.append(user)
    user_db.close()
    user_db = open(USER_DATABASE_FILE, 'w')
    user_db.write(json.dumps(user_list))
    user_db.close()
    return True


# TODO Check the password to a more secure way to achieve
# TODO Consider the password with SHA256(or other) encryption
def login(user):
    """
    :param user: (dict)["user_id","password"]
    :return: true/false
    """
    user_db = open(USER_DATABASE_FILE, 'r')
    user_list = json.loads(user_db.read())
    user_db.close()
    # Inspection id exists and verify the password
    for pre_user in user_list:
        if user['user_id'] == pre_user['user_id']:
            if user['password'] == pre_user['password']:
                return True

    return False


def set_user_information(user_info):
    """
    Set up user information
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
    Get user information
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
    Detects whether the id appears in the database
    :param id:
    :param list_to_check: 
    :return: true/false
    """
    for x in list_to_check:
        if x['user_id'] == id:
            return True

    return False
