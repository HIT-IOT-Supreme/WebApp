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
    
## 相关API

### 心知天气

`test/weather.py`为测试脚本。此处点击[API doc](http://www.thinkpage.cn/doc)。

### 知乎日报

`test/zhihu.py`为测试脚本。此处点击[API doc](https://github.com/izzyleung/ZhihuDailyPurify/wiki/%E7%9F%A5%E4%B9%8E%E6%97%A5%E6%8A%A5-API-%E5%88%86%E6%9E%90)。