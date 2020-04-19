#### 项目总结

## 1、生成一个项目
* 安装Python，Pip，安装Django后并且检查相关版本
* 新建Django项目的命令 django-admin startproject HelloWorld
* 连接mysql数据库 否者会报错 注释数据库相关配置代码就可以正常 pip install mysqlclient
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
+ 

## 4、数据库的安装步骤

+ 填写数据库的基本信息
<<<<<<< HEAD
+ 安装数据库驱动pip install pymysql / pip install mysqlclient 解决了问题
+ 
=======
+ 安装数据库驱动pip install pymysql[旧的驱动]
+ C:\Users\pc\AppData\Local\Temp\pip-install-d864pdal\mysqlclient\
+ 更换驱动<https://www.jianshu.com/p/e21a57bdd2fb>

```
C:\Users\pc\AppData\Local\Programs\Python\Python37-32\Scripts\;C:\Users\pc\AppData\Local\Programs\Python\Python37-32\;
mysql -uroot -proot #开启数据库
mysql --version #检查数据库版本
#my.ini中修改端口
```
+ phpStudy 
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

```
C:\Program Files (x86)\Common Files\Oracle\Java\javapath;C:\Ruby25-x64\bin;C:\Program Files (x86)\Intel\iCLS Client\;C:\Program Files\Intel\iCLS Client\;C:\windows\system32;C:\windows;C:\windows\System32\Wbem;C:\windows\System32\WindowsPowerShell\v1.0\;C:\Program Files (x86)\Intel\UCRT\;C:\Program Files\Intel\UCRT\;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files (x86)\NVIDIA Corporation\PhysX\Common;C:\Program Files\Git\cmd;D:\myphp_www\PHPTutorial\php\php-7.2.1-nts;C:\composer;C:\ProgramData\chocolatey\bin;C:\Program Files\nodejs\;C:\Program Files\TortoiseGit\bin;C:\Program Files (x86)\Bitvise SSH Client;D:\Android\android-sdk\platform-tools;%systemroot%\System32\WindowsPowerShell\v1.0\;D:\Android\android-sdk\platform-tools;C:\Users\pc\.gradle\wrapper\dists\gradle-5.4.1-all\3221gyojl5jsh0helicew7rwx\gradle-5.4.1\bin;D:\MySQL\MySQL Server 5.7\bin;
```
+ 数据库安装后的解决方案<https://blog.csdn.net/chen97_08/article/details/81484286>
+ 升级mysql<https://blog.csdn.net/yt_php/article/details/81302367>
```
[client]
port=3306
[mysql]
default-character-set=utf8
[mysqld]
port=3306
basedir="D:/soft/phpstudy/PHPTutorial/MySQL/"
datadir="D:/soft/phpstudy/PHPTutorial/MySQL/data/"
character-set-server=utf8
default-storage-engine=INNODB

max_connections=512

query_cache_size=0
tmp_table_size=32M

thread_cache_size=8
myisam_max_sort_file_size=64G
myisam_sort_buffer_size=35M
key_buffer_size=25M
read_buffer_size=64K
read_rnd_buffer_size=256K
sort_buffer_size=256K

innodb_additional_mem_pool_size=2M

innodb_flush_log_at_trx_commit=1
innodb_log_buffer_size=1M

innodb_buffer_pool_size=47M
innodb_log_file_size=24M
innodb_thread_concurrency=8
#新加
innodb_file_per_table = 1
skip-grant-tables = 1 #跳过权限验证
log-error = D:/soft/phpstudy/PHPTutorial/MySQL/data/error.log

```
+ 创建管理用户
+ python manage.py createsuperuser
+ user:admin
+ password:root
+ email:768449566@qq.com

+ 如果你有一个模板文件正好和另一个应用中的某个模板文件重名，Django 没有办法 区分 它们

>>>>>>> f326878102861a112942502b1cca4b1019e460c3
