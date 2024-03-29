"""
Django settings for MyDjango project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

#项目路径
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

#密钥配置
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7q50rdp#%hj*(u$b&42e%v@a_jiq0--hyzc28f)-hny8g1=24g'

# SECURITY WARNING: don't run with debug turned on in production!
#调试模式
DEBUG = True
#域名访问权限
ALLOWED_HOSTS = ['*']

#app 列表
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    #静态资源查找
    'django.contrib.staticfiles',
    'index',
    'user',
]

#中间件:处理Django的request和response对象的钩子
#每个中间件的设置顺序是固定的，如果随意变更中间件很容易导致程序异常
MIDDLEWARE = [
    #内置的安全机制
    'django.middleware.security.SecurityMiddleware',
    #会话Session功能
    'django.contrib.sessions.middleware.SessionMiddleware',
    #使用中文
    'django.middleware.locale.LocaleMiddleware',
    #处理请求信息，规范化请求内容
    'django.middleware.common.CommonMiddleware',
    #开启CSRF防护功能
    'django.middleware.csrf.CsrfViewMiddleware',
    #开启内置的用户认证系统
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #开启内置的信息提示功能
    'django.contrib.messages.middleware.MessageMiddleware',
    #防止恶意程序点击劫持
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MyDjango.urls'

#模板
TEMPLATES = [
    {
        #定义模板引擎，用于识别模板里面的变量和指令
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #设置模板所在路径，告诉django在哪个地方查找模板的位置
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, '/index/templates')],
        #是否在app里查找模板文件
        'APP_DIRS': True,
        #用于填充在RequestContext中上下文的调用函数，一般情况下不做任何修改
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MyDjango.wsgi.application'


#数据库
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    #第一个数据库
    'default': {
        #sqlite3是一款轻型的数据库，常用于嵌入式系统开发，而且占用的资源非常少
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT':'3306',
        'NAME':'django_db',
        'USER':'root',
        'PASSWORD':'test',
    },
    # #第二个数据库
    # 'MyDjango': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'HOST': '127.0.0.1',
    #     'PORT':'3306',
    #     'NAME':'MyDjango_db',
    #     'USER':'root',
    #     'PASSWORD':'1234',
    # },
    # #第三个数据库
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # },
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#静态资源配置
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'

#设置根目录的静态资源文件夹public_static
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'public_static'),
                    #设置app（index）的静态资源文件夹index_static
                    os.path.join(BASE_DIR, 'index/index_static')]
#方便在服务器上部署项目，实现服务器和项目之间的映射
STATIC_ROOT = os.path.join(BASE_DIR, 'all_static')