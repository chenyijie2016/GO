Introduction
============

目录说明
--------

前端围棋棋盘---tenuki.js
~~~~~~~~~~~~~~

* static/:返回的网页文件
* static/go.html:主网页
* static/login.html:登录界面
* static/register.html:注册界面

后端---flask
~~~~~~~~~~~~~~

* server.py:服务端主进程,可以添加与前端对应的通信模块,所有接收到的需要处理的信息都会发送到gamemain.py中进行处理
* gamemain.py:负责处理分发所有信息
* game_function.py:负责处理对局信息
* user.py:负责用户登录、注册、信息更新保存的方面
* blockchain.py:负责区块链数据处理(等待合并)
* AI.py:AI接口(等待合并)
* (未完待更新)

数据库部分---mongodb
~~~~~~~~~~~~~~~~~~~~~~~~
* 注意,以下所有数据库均为临时解决方案

* user_database/:与用户有关的数据库
* user_database/user_list.db:存储用户名和密码对
* user_database/user_info.db:存储用户信息

* game_database/:游戏记录数据库
* game_database/sgf/:sgf文件的存储目录，sgf文件以对应的game_id命名
* game_database/game_status.db:存储所有的对局信息

