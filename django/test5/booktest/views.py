from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

# Create your views here.

EXCLUDE_IPS = ['192.168.1.105']
def blocked_ips(view_func):
    def wrapper(request, *view_args, **view_kwargs):
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in EXCLUDE_IPS:
            return HttpResponse('<h1>禁止访问</h1>')
        else:
            return view_func(request, *view_args, **view_kwargs)

    return blocked_ips



EXCLUDE_IPS = ['192.168.1.105']
def index(request):
    print(settings.STATICFILES_FINDERS)
    user_ip = request.META['REMOTE_ADDR']
    print('客户端的ip： '+user_ip)
    if user_ip in EXCLUDE_IPS:
        return HttpResponse('<h1>禁止访问</h1>')
    return render(request, 'booktest/index.html')