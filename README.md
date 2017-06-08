### 项目文档:http://nand2x-go.readthedocs.io

### 项目永久地址：[围棋测试2.0](http://123.206.72.191:8080)

#### 运行方法更新：

1. 启动根目录下server.py

2. 启动MuGo目录下server.py

> 可将MuGo目录单独分离出来，两者不需要在一个环境中，只需要建立网络连接，关于kubernetes的网络配置我还不清楚

> 两者均使用flask环境,数据传输使用本地6000端口,如需修改url及端口可到根目录下AI.py以及MuGo目录下server.py中修改(均有注释提示)

> 现在网页端环境中不再需要tensorflow

#### BUG暂时汇总

* BUG紧急修复须知:根目录及MuGo目录下game_database文件夹中需增加sgf文件夹,否则会报错

## 说明：
  本项目从现在起可能会暂停更新了,现在网页端还有着各种各样的BUG，整体架构也有各种各样的缺陷，不过我们会一直维护下去，即使时间很长，一个完整的围棋网站项目一定会完成!
