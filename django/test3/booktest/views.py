from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from datetime import datetime, timedelta

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
    # 获取cookie用户名
    if 'username' in request.COOKIES:
        # 获取记住的用户名
        username = request.COOKIES['username']
    else:
        username = ''
    return render(request, 'booktest/login.html', {'username': username})

def login_check(request):
    '''登录校验视图'''
    # request.POST
    # request.GET
    # 1. 获取提交的用户名密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    print(remember)
    if username == 'tree' and password == '123456':
        # 用户名正确，跳转首页
        response = redirect('/index')  # 就是HttpResponse子类对象
        # 判断是否需要记住用户名
        if remember == 'on':
            response.set_cookie('username', username, max_age=7*24*3600)
        return response
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

def login_ajax(request):
    '''显示ajax登录页面'''
    return render(request, 'booktest/login_ajax.html')

def login_ajax_check(request):
    '''ajax登录校验'''
    # 1。 获取用户名密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'tree' and password == '000':
        return JsonResponse({'res': 1})
    else:
        return JsonResponse({'res': 0})
    # 2. 进行校验，返回json数据
    # 3.

# /set_cookie
def set_cookie(request):
    '''设置cookie'''
    response =  HttpResponse('设置cookie')
    response.set_cookie('num', 1, max_age=14*24*3600)
    # response.set_cookie('num', 1, expires=datetime.now().timedelta(days=14))
    return response
# /get_cookie
def get_cookie(request):
    '''获取cookie'''
    num = request.COOKIES['num']
    return HttpResponse(num)

# /set_session
def set_session(request):
    '''设置session'''
    request.session['username'] = 'tree'
    request.session['age'] = 24
    return HttpResponse('设置Session')

# /get_session
def get_session(request):
    '''获取session'''
    username = request.session['username']
    age = request.session['age']
    return HttpResponse(username+':'+str(age))

# /clear_session
def clear_session(request):
    '''清除session信息'''
    request.session.clear()
    return HttpResponse('清楚session成功')





























