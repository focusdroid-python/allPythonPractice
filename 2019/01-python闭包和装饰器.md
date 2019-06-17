## 闭包
    > 0.函数内部嵌套函数
    > 1.内部用到了外部的局部变量
   ```
    def line(k, b):
        def create(x):
            print(k*x+b)
        return create
        
    line_arg = line(1,2)
    line_arg(0)
    line_arg(1)
    line_arg(2)
    
   ```
## 闭包内部修改局部变量
>0. 闭包修改局部变量需要加上nonlocal 
      
  ```
    x = 300

    def test1():
        x = 200
        def test2():
            nonlocal x
            print('-------1---x = %d:'%x)
            x = 100
            print('-------2---x = %d:'%x)
        return test2
  ```   
    
    
## 装饰器
   ```
        def set_fun(func):
            def call_fun():
                print('------权限验证111----')
                print('------权限验证222----')
                func()
            return call_fun
        
        @set_fun
        def test():
            print('-----------test1-------------')
        
        
        test()
   ```
## 多个装饰器装饰的顺序
    >0. 
    >1.
    >2.
    >3.
    ```
       def add_qx(func):
            print('-------开始执行权限111--------')
            def call_fun(*args, **kwargs):
                print('--------权限验证1111------')
                return func(*args, **kwargs)
            return call_fun
        
        
        def add_qxs(func):
            print('-------开始执行权限222--------')
            def call_fun(*args, **kwargs):
                print('--------权限验证2222------')
                return func(*args, **kwargs)
            return call_fun
        
        
        @add_qx
        @add_qxs
        def test():
            print('-----------test--------------')
        
        test()
        
        
        ------开始执行权限222--------
        -------开始执行权限111--------
        --------权限验证1111------
        --------权限验证2222------
        -----------test--------------
        
        > 0.两个装饰器对函数进行装饰，先执行离函数近的

    ```
    
## 带有参数装饰器
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    