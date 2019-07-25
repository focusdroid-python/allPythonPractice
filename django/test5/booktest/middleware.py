from django.http import HttpResponse


class BlockedIPSMiddleware(object):
    '''中间'''
    EXCLUDE_IPS = ['192.168.1.105']
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        ''' 视图函数调用之前'''
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in EXCLUDE_IPS:
            return HttpResponse('<h1>禁止访问</h1>')
        else:
            return view_func(request, *view_args, **view_kwargs)