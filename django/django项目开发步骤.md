## 初始化项目
    > django-admin startproject 项目名字
    > django-admin startproject test
    
## 创建应用
    >  进入项目  cd test3
    > python manage.py startapp 应用名称
    > python manage.py startapp booktest
    
## 注册应用
    > 选择settings 文件
    > 在 INSTALLED_APPS 中添加应用名
    > 'booktest'
    
## 创建模板
    > 在根目录创建 template文件夹
    > 在 settings中TEMPALTES / 'DIRS': [os.path.join(BASE_DIR, 'templates')]
## 设置数据库
    > 在 settings中 DATABASES 
    ```
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
        修改为
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql', # 使用mysql数据库
                'NAME': 'bi18', # 数据库名字
                'USER': 'root',
                'PASSWORD': 'mysql',
                'HOST': 'localhost',
                'PORT': 3306
                
            }
        }
        
        在test3/tests/__init__.py添加如下
        import pymysql
        pymysql.install_as_MySQLdb()
    ```
## 创建HTML模板
    > 在templates文件夹中创建booktest文件夹
    > 在booktest文件夹创建index.html
    >  
    >  
    >  
    >  
## 创建统一管理的urls
    > 在test3/test3中的urls加入以下
    > url(r'^', include('booktest.urls')),
    > 在test3/booktest/创建urls集中管理url
        > 在booktest/urls添加index的路由
    ```
        from django.conf.urls import url
        from booktest import views
        
        urlpatterns = [
            url(r'^index$', views.index), # 首页
        ]
    ``` 
    > 定义视图:
        > 在test3/booktest/views.py添加如下
        ```
            def index(request):
            '''首页'''
            return render(request, 'booktest/index.html')
        ```
    > 运行项目 python manage.py runserver
    > 修改404错误页面
        You're seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard 404 page.
        就是将settings里面的DEBUG = false
        并且ALLOWED_HOSTS = ['*']
        你也可以自己定义404页面，
        在templates/新建404.html系统自动会将这个页面显示
        可以用resquest_path获取用户访问的路径
    > 500页面
        在templates/新建500.html系统自动会将这个页面显示
## 捕获URL参数
    views.py
        def show_arg(request, num):
            return HttpResponse(num)
    urls.py
        url(r'^showarg(\d+)$', views.show_arg), # 捕获url参数
    访问/showarg11
    > 2. 关键字参数
        ?p<组名>
        关键字参数，视图中参数名必须和正则表达式组名一致
        views.py
            def show_many(request, num):
                return HttpResponse(num)
        urls.py
            url(r'^showmany(?P<number>\d+)$', views.show_many ), # 捕获url参数,关键字参数
        ?p<组名>
        关键字参数，视图中参数名必须和正则表达式组名一致 
## 登录案例
    request对象属性
        # request.POST QueryDict
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
    如果有CSRF错误 注释settings/MIDDLEWARE_CLASSES元祖的 'django.middleware.csrf.CsrfViewMiddleware',

## 在项目中使用静态文件(项目具体文件在test3中)
    在根目录新建static文件夹
    在settings中最底部添加
        STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] # 是静态文件的保存目录
        
## ajax登录案例
    > 1. 首先分析出请求地址时需要携带的参数
    > 2. 视图函数处理完成之后，所返回json的格式

## 设置cookie
    > 1. 需要一个HttpResponse对象或者它子类对象
        ```
        from datetime import datetime, timedelta
            # /set_cookie
            def set_cookie(request):
                '''设置cookie'''
                response =  HttpResponse('设置cookie')
                # 设置多少妙之后过期
                response.set_cookie('num', 1, max_age=14*24*3600)
                # 设置多少天之后过期
    r           esponse.set_cookie('num', 1, expires=datetime.now().timedelta(days=14))
                return response
            # /get_cookie
            def get_cookie(request):
                '''获取cookie'''
                num = request.COOKIES['num']
                return HttpResponse(num)

        ```
## 设置session
    设置session session.request.session['username'] = 'wangxu'
    获取session session.request.session['username']
    清楚所有session，在存储中删除值部分
        request.session.clear()
    清除session数据，在存储中删除session的整条数据
        request.session.flush()
    删除session中的指定键及值，在存储中只删除对应的值
        del request.session['key']
    设置session过期时间，如果没有指定时间则两个星期后过期
        request.session.set_expiry(value)
         
         
## 模板变量
    模板变量是由数字字母下划线和点组成【不能以下划线开头，使用模板变量{{模板变量}}】
    例如： {{book.btitle}}
    例如： {{book.0}}
        1. 首先把book当成一个字典，把0当成键名，进行取值book[0]
        2. 把book当成一个列表，把0当成下标，进行取值nook[0]
        book[0]
    使用模板变量时，前面可能会是一个字典，可能是一个对象，还可能是一个列表
        
## 模板标签

## 模板继承
    > 1. {% extends 'booktest/base.html' %}
        继承之后不能写其他内容
    > 2. 预留块
        {% block 块名 %}
            可以写内容也可以不写内容
        {% endblock 块名 %}
        
## 图片验证码
    pip install Pillow==3.4.1
    pillow安装报错：
        https://blog.csdn.net/shaququ/article/details/54292017

## url反向代理
    在test4/test4/urls.py中： namespace一般和项目文件夹名字一致
        url(r'^', include('booktest.urls', namespace='booktest')),
        
## django静态资源路径
    # 设置访问静态文件的地址
    STATIC_URL = '/static/'
    # 设置静态文件的物理目录
    STATICFILEs_DIRS = [os.path.join(BASE_DIR, 'static')]
    ## 使用setting获取图片路径（静态资源）
    from django.conf import settings
    print(settings.STATICFILES_FINDERS)
        ('django.contrib.staticfiles.finders.FileSystemFinder', 'django.contrib.staticfiles.finders.AppDirectoriesFinder')

## 中间件
    # 中间件函数是django框架给我们预留的函数接口，让我们可以敢于请求和应答过程
    # 获取客户端ip
   request.META['REMOTE_ADDR']
   # 禁止ip访问页面
    EXCLUDE_IPS = ['192.168.1.105']
    def index(request):
        print(settings.STATICFILES_FINDERS)
        user_ip = request.META['REMOTE_ADDR']
        print('客户端的ip： '+user_ip)
        if user_ip in EXCLUDE_IPS:
            return HttpResponse('<h1>禁止访问</h1>')
        return render(request, 'booktest/index.html')
    # 使用装饰器
    EXCLUDE_IPS = ['192.168.1.105']
    def blocked_ips(view_func):
        def wrapper(request, *view_args, **view_kwargs):
            user_ip = request.META['REMOTE_ADDR']
            if user_ip in EXCLUDE_IPS:
                return HttpResponse('<h1>禁止访问</h1>')
            else:
                return view_func(request, *view_args, **view_kwargs)
    
        return blocked_ips
        
    ## 使用middleware限制ip访问：
        在test5/booktest新建middleware.py
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
                    
        注册middleware(settings/MIDDLEWARE):
            'booktest.middleware.BlockIPSMiddleware', # 注册中间见类
            
    ## django预留的中间件函数
    __init__: 服务器相应第一个请求的时候调用
    precess_request: 在产生request对象，进行url匹配之前调用
    process_view: 在url匹配之后，调用视图函数
    precess_response: 视图函数调用之后，内容返回给浏览器之前
    precess_exception:视图函数出现异常，会调用这个函数
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    