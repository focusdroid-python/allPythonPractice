from django.conf.urls import url
from booktest import views
urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^index2$', views.index2),
    url(r'^temp_var$', views.temp_var),
    url(r'^verify_code$', views.verify_code),
    url(r'^url_reverse$', views.url_reverse), # url反向解析页面
    url(r'^show_arg/(\d+)/(\d+)$', views.show_arg, name='show_arg'), # 捕获位置参数
    url(r'^show_kwargs%/(?P<c>\d+)/(?P<d>\d+)', views.show_kwargs, name='show_kwargs'), # 关键字参数
]