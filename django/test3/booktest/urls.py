from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index$', views.index), # 首页
    url(r'^showarg(\d+)$', views.show_arg), # 捕获url参数，位置参数
    url(r'^showmany(?P<number>\d+)$', views.show_many ), # 捕获url参数,关键字参数
    url(r'^getResquest', views.get_resquest), # 捕获url参数,关键字参数
    url(r'^login$', views.login), # 登录页面
    url(r'^login_check', views.login_check), # request对象接收参数
    url(r'^test_ajax$', views.ajax_test), # 显示ajax页面
    url(r'^ajax_handle$', views.ajax_handle), # ajax处理
    url(r'^loginAjax$', views.login_ajax),
    url(r'^login_ajax_check$', views.login_ajax_check),
    url(r'^set_cookie$', views.set_cookie),
    url(r'^get_cookie$', views.get_cookie),
    url(r'^set_session$', views.set_session),
    url(r'^get_session$', views.get_session),
    url(r'^clear_session$', views.clear_session),
]
