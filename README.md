# web_app

## 开发准备

建议在`virtualenv`虚拟环境下进行开发，使用如下代码进行虚拟环境的安装：

    pip install virtualenv

使用`virtualenv`指令在该项目的根目录下安装虚拟环境：

    virtualenv venv
    
启动虚拟环境：

    . venv/bin/activate
    
> 以上指令在ubuntu下测试可用，在Windows下需要在`scripts`目录下寻找`activate`

在虚拟环境下安装依赖：

    pip install -r requirements.txt
    
启动工程：

    python run.py 
    
## 部署说明

本项目使用`flask+gunicorn+supervisor`方案进行部署。    
其中`supervisor`的基本使用命令如下：

```
supervisord -c supervisor.conf                             通过配置文件启动supervisor
supervisorctl -c supervisor.conf status                    察看supervisor的状态
supervisorctl -c supervisor.conf reload                    重新载入 配置文件
supervisorctl -c supervisor.conf start [all]|[appname]     启动指定/所有 supervisor管理的程序进程
supervisorctl -c supervisor.conf stop [all]|[appname]      关闭指定/所有 supervisor管理的程序进程
```
    
## 相关API

### 心知天气

`test/weather.py`为测试脚本。此处点击[API doc](http://www.thinkpage.cn/doc)。

### 知乎日报

`test/zhihu.py`为测试脚本。此处点击[API doc](https://github.com/izzyleung/ZhihuDailyPurify/wiki/%E7%9F%A5%E4%B9%8E%E6%97%A5%E6%8A%A5-API-%E5%88%86%E6%9E%90)。

### 图灵机器人

`test/turing_robot`为测试脚本。此处点击[API doc](http://www.tuling123.com/help/h_cent_webapi.jhtml)。

### 极光推送

`test/jpush`为测试脚本。此处点击[API doc](http://docs.jiguang.cn/jpush/server/push/rest_api_v3_push)。