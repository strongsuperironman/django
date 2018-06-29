mkvirtualenv python1806 -p/usr/bin/python3#创建虚拟环境
rmvirtualenv python1806#删除虚拟环境
workon python1806#进入虚拟环境
pip install django==1.11.7#下载django
pip freeze #查看是否安装成功
mkdir python1806#创建工作文件夹
cd python1806#进入工作文件夹
django-admin startproject HelloDjango#创建django工程
ls#查看是否创建成功
cd HelloDjango #进入工程文件中
ls#查看是否有manage.py文件如果有则创建成功
python manage.py runserver#启动服务器
python manage.py startapp App#创自己的APP
#打开pycharm进入工程在setting中进项编译环境的配置
setting.py中的配置
ALLOWED_HOSTS = ['*']#*代表允许任何人访问
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'App'
]#添加自己的App
'DIRS': [os.path.join(BASE_DIR,'templates')],#添加模板环境
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
         'ENGINE':'django.db.backends.mysql',
         'NAME':'peopleDjango',
          'USER':'root',
         'PASSWORD':'199416lz',
          'HOST':'localhost',
          'PORT':'3306'
    }
}#添加myaql
LANGUAGE_CODE = 'zh-hans'#把英文改为汉字
TIME_ZONE = 'Asia/Shanghai'#把时间改为中国时间

在APP下创建urls.py
url(r'^app/',include('App.urls',namespace="python1806"))#在系统url.py中配置,导入include包,namespace的作用是用在反向解析中
from django.conf.urls import url
from App import views
urlpatterns=[
    url(r'getstu/',views.get_age_and_grade,name="liuzhen")]#在App中配置url,name用在反向解析中
配置mysql
1.安装mysql
 pip install pymysql
2.创建mysql
 进入mysql -u root -p密码
创建库
在__init__中进行初始化
 import pymysql
      pymysql.install_as_MYAQLDB()
