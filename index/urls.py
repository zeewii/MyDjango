"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#index的urls.py
from django.urls import path, re_path
from . import views
#index app的URL集合，每个元素代表一条URL信息
urlpatterns = [
    # 首页的URL
    path('', views.index),
    path('login.html', views.login),
    #通用视图ListView
    # path('index/', views.ProductList.as_view()),
    path('index/<id>.html', views.ProductList.as_view(),{'name':'phone'}),
    # path('<year>/<int:month>/<slug:day>', views.mydate),
    # #正则表达式的路径
    # # re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html', views.mydate)
    # re_path(r'^(?P<year>[0-9]{4}).html', views.myyear, name='myyear'),
    # #参数为字典的URL,设置额外参数
    # re_path(r'^dict/(?P<year>[0-9]{4}).html', views.myyear_dict, {'month':'05'}, name='myyear_dict'),
    path('download.html', views.download)
]
