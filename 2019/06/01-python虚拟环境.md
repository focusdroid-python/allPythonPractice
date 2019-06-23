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
    ****编码与解码****
    ```
        import urllib
        
        urllib.parse.quote('中国') // %E4%B8%AD%E5%9B%BD
        urllib.parse.unquote('%E4%B8%AD%E5%9B%BD') // 中国
        
        
    ```