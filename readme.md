#### 项目总结

* 安装Python，Pip，安装Django后并且检查相关版本
* 新建Django项目的命令 django-admin startproject HelloWorld
* 连接mysql数据库 否者会报错 注释数据库相关配置代码就可以正常 pip install mysqlclient
* 运行Django项目的命令 python manage.py runserver 8080
* 时间：2019-09-10号开始开发mvc框架相关的web网站

#### 项目运行

1. Django设置允许跨域的问题<https://blog.csdn.net/zhu6201976/article/details/84677213>
2. http请求响应过程中的三次握手四次挥手<https://www.jianshu.com/p/bd31d3b23725>
3. 此处为服务端（使用python中的web框架django）

+ 使用Pip安装Django框架依赖环境
+ python -> pip -> django
+ Django2.0官方文档<https://docs.djangoproject.com/zh-hans/2.2/>
+ python版本<Python 3.6.16>
+ django版本<2.2.23>
+ 安装跨域的依赖包
```
pip install django-cors-headers

```
+ 生成一个项目【新生成局部项目】
```
python manage.py startapp projectName

```

+ 下载镜像<http://npm.taobao.org/mirrors/python/3.7.4/>
+ amd64
+ 直播项目

#### 数据库的安装步骤

+ 填写数据库的基本信息
+ 安装数据库驱动pip install pymysql / pip install mysqlclient 解决了问题
+ 