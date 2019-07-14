from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    '''首页'''
    # num = 'a' + 1
    return render(request, 'booktest/index.html')

def show_arg(request, num):
    return HttpResponse(num)

def show_many(request, number):
    return HttpResponse(number)

def get_resquest(request):
    return HttpResponse(request)

def login(request):
    '''登录'''
    return render(request, 'booktest/login.html')

def login_check(request):
    '''登录校验视图'''
    # request.POST
    # request.GET
    # 1. 获取提交的用户名密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username+':'+password)
    if username == 'tree' and password == '123456':
        # 用户名正确，跳转首页
        return redirect('/index')
    else:
        # 用户名或密码错误，跳转登录页面
        return redirect('/login')
    # 2. 进行登录的校验
    # 3. 返回应答
    return HttpResponse('ok')

# ajax page
def ajax_test(request):
    '''显示ajax页面'''
    return render(request, 'booktest/test_ajax.html')

def ajax_handle(request):
    '''ajax请求处理'''
    # 返回json数据
    return JsonResponse({'code': 200})