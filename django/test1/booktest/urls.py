from django.conf.urls import url
from booktest import views

urlpatterns = [
    # 通过url函数设置url路由配置
    url(r'^index$', views.index), # 建立/index和视图index之间的关系, $严格匹配结尾
    url(r'^login$', views.login), # 建立/index和视图index之间的关系
]