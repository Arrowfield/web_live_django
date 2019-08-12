#### 项目总结

## 1、生成一个项目
* 安装Python，Pip，安装Django后并且检查相关版本
* 新建Django项目的命令 django-admin startproject HelloWorld
* 运行Django项目的命令 python manage.py runserver 8080
* 时间：2019-09-10号开始开发mvc框架相关的web网站

## 2、项目运行

1. Django设置允许跨域的问题<https://blog.csdn.net/zhu6201976/article/details/84677213>
2. http请求响应过程中的三次握手四次挥手<https://www.jianshu.com/p/bd31d3b23725>
3. 此处为服务端（使用python中的web框架django）

+ 使用Pip安装Django框架依赖环境
+ python -> pip -> django
+ Django2.0官方文档<https://docs.djangoproject.com/zh-hans/2.2/>
+ python版本<3.6.16>
+ django版本<2.2.23>
+ mysql版本<5.5>
+ pip版本<19.0.3>
+ 安装跨域的依赖包
+ 每个子项目彼此独立
```
pip install django-cors-headers

```

## 3、生成子项目

+ 生成一个项目【新生成局部项目】
```
python manage.py startapp projectName

```
+ 下载镜像<http://npm.taobao.org/mirrors/python/3.7.4/>
+ amd64
+ 直播项目
+ msi

## 4、数据库的安装步骤

+ 填写数据库的基本信息
+ 安装数据库驱动pip install pymysql[旧的驱动]
+ C:\Users\pc\AppData\Local\Temp\pip-install-d864pdal\mysqlclient\
+ 更换驱动<https://www.jianshu.com/p/e21a57bdd2fb>

```
C:\Users\pc\AppData\Local\Programs\Python\Python37-32\Scripts\;C:\Users\pc\AppData\Local\Programs\Python\Python37-32\;
mysql -uroot -proot #开启数据库
mysql --version #检查数据库版本
#my.ini中修改端口
```
+ phpStudy mysql版本升级<https://www.csdn.net/gather_24/MtTaIg1sNDg4My1ibG9n.html>
+ 数据库安装成功

## 5、建立Models
+ 创建模型
+ 激活模型
```
python manage.py makemigrations live #激活模型
python manage.py sqlmigrate live 0001 #生成sql语句
python manage.py check #检查问题 
python manage.py migrate #创建数据表

```
+ 备注 生成的表明：【子应用名_类名】


