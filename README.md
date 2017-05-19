本周任务

1.网站页面的css设计

2.网站模块的添加

*2.1用户登录信息模块(采用cookie保存登录信息,具体可参考login.html)
*2.2用户信息数据模块(已有user_list.db数据库文件,参考user.py中方法进行储存和修改用户信息)
*2.3用户数据显示模块(新建一个页面，显示当前用户的信息,参考register.html 和 login.html)
*2.4对战信息显示模块(实时显示未开始和已经开始的游戏，在网站中添加一个显示数据的地方)
*2.5对局信息记录(已有记录到sgf文件中，考虑新建一个数据库,存储摘要信息)
*AI接口
2.6从sgf加载对局信息（先放放）
2.7bug修复与测试


相关教程
Python flask：
http://docs.jinkan.org/docs/flask/index.html(必读）

JavaScript jQuery:
http://www.w3school.com.cn/jquery/index.asp（必读）

关于 CSS3 或者 Bootstrap CSS库 的教程
http://www.bootcss.com/
http://www.w3school.com.cn/css3/index.asp


详细说明

目录说明：

根目录：游戏逻辑脚本
html:返回的网页文件
user_database:与用户有关的数据库
game_database:游戏记录数据库


逻辑处理部分：

server.py:服务端主进程,可以添加与前端对应的通信模块,信息处理在其他文件中实现
gamemain.py:负责处理与对局有关的信息
user.py:负责用户登录、注册、信息更新保存的方面
blockchain.py:负责区块链数据处理(尚未实现)
AI.py:AI接口(尚未实现)
(未完待更新)


数据库部分:
user_list.db:存储用户名、密码等信息
game_status.db:存储所有对局信息




