# 项目文档:http://nand2x-go.readthedocs.io


# 目录说明

## 前端---tenuki.js
- static/:返回的网页文件

## 后端---flask
- server.py:服务端主进程,可以添加与前端对应的通信模块,信息处理在其他文件中实现
- gamemain.py:负责处理与对局有关的信息
- user.py:负责用户登录、注册、信息更新保存的方面
- blockchain.py:负责区块链数据处理(尚未实现)
- AI.py:AI接口(尚未实现)
- (未完待更新)

## 数据库部分---mongodb
- user_database/:与用户有关的数据库
- game_database/:游戏记录数据库

# 相关教程
Python flask：
http://docs.jinkan.org/docs/flask/index.html(必读）

JavaScript jQuery:
http://www.w3school.com.cn/jquery/index.asp（必读）

关于 CSS3 或者 Bootstrap CSS库 的教程
http://www.bootcss.com/
http://www.w3school.com.cn/css3/index.asp

