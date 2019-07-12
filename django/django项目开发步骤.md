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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    