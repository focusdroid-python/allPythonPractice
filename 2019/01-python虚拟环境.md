### 安装虚拟环境的命令
    > 0. sudo pip3 install virtualenv  安装虚拟环境
    > 1. sudo pip3 install virtualenvwrapper  安装虚拟环境扩展包
    > 2. 编辑家目录下的.bashrc文件，添加下面两行代码
    ```
        export WORKON_HOME=$HOME/.virtualenvs
        source /usr/local/bin/virtualenvwrapper.sh
    ```
    > 3. 使用source .bashrc使其生效一下
    > 4. 
    ```
        4.1 创建虚拟环境命令
            mkvirtualenv 虚拟环境名
        4.2 创建python3的虚拟环境
            mkvirtualenv -p -python3 虚拟环境的名字
        4.3 进入虚拟环境
            workon 虚拟环境名
        4.4 退出虚拟环境
            deactivate
        4.5 查看机器上有多少虚拟环境
            workon 空格 + 两个Tab键
        4.6 删除虚拟环境
            rmvirtualenv 虚拟环境名称
        4.7 查看虚拟环境装了那些包
            pip list 
    ```
    > 5. 在虚拟环境安装一些包【不能使用sudo pip install 包名】
        pip install django==1.8.2
        ```
            pip list
            pip freeze [显示格式,在发布的时候又用]
        ```
    ***ctrl + h --> 显示隐藏文件夹***
    
##项目创建
   ```
      
      0. django-admin startproject test
      
      __init__.py 说明test1是一个python包
      settings.py 项目配置文件
      urls.py     进行url路由的配置
      wsgi        web服务器和Django交互的入口
      manage.py   项目的管理文件
      
      ## 在Django,每一模块使用一个django应用来开发
      ## 一个项目由很多应用组成，每一个应用完成一个特定功能
      创建应用命令如下：
            python manage.py startapp 应用名
            python manage.py startapp booktest
      **创建应用时需要进入项目目录   **
      booktest
        __init__.py 说明目录是一个python模块
        models.py   写数据库项目的内容
        views.py    接收请求，请求处理，与T和M进行交互，返回应答。定义处理函数视图函数
        tests.py    测试代码
        admin.py    网站后台管理相关的文件
        
        修改setting.py中的INSTALLED_APPS
        建立应用和项目之间的联系，需要对应用进行注册
   ```
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    