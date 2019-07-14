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
    
         
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    