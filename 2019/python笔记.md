### python中的copy (import copy)
    >0. copy.copy() 浅拷贝
    >1. copy.deepcopy() 深拷贝
    `
        a = [11,22]
        b = [33,44]
        c = [a,b]
        d = copy.copy(c)
        e = copy.deepcopy(c)
        c.append([66,77])
        c [[11,22],[33,44],[66,77]]
        d [[11,22],[33,44]] copy的对象是a和b
        e [[11,22],[33,44]]
    ```
    > 如果不可变里边的数据都是不可变的就是简单指向
### 私有化
    > xx 公有变量
    > _x 私有化属性或方法，from somemodule import * 禁止导入，类和子类可以访问
    > __xx 私有，无法在外部访问
    > __xx__ 用户名字空间的魔法对象或属性,可以在外部访问
    > xx_ 用于避免与python关键词冲突
    >
### import 模块导入
    > 0. 重新导入模块【from imp import reload  reload(模块名)】
    > 
### 多继承中的MRO顺序(调用顺序)
    > 类名.__mro__   查看super调用的顺序
    
### python中的参数
    > def __init__(self, *args, **kwargs)
    > def __call__(self, *args, **kwargs)
    ```
        class Foo：
            def __call__(self, *args, *kwargs):
                print('__call__')            
        obj = Foo()
        obj() # 直接调用call方法
    ```
    > __dict__ # 能检测类和所有私有属性
    > __str__  # 获取对象的描述时，
    
### python中的类对象 实例对象  类属性 实例属性 类方法, 实例方法  静态方法
    > __new__ 创建对象,开辟内存空间(默认是随机的数据)
    > __init__ 对刚刚的空间初始化
    > classmethod  类方法(修改类属性， cls指向类对象)
    ``
        @classmethod
        def class_fun(cls):
            print('类方法')
        
     ```
    > staticmethod  静态方法(不需要传参数，易于归类管理)
    ```
        def static_func():
            print('静态方法')
    ```
    > 实例方法(就是一般的方法，self指向实例对象)
    ```
       def ord_func(self):
            print('实例方法')
    ```   
    > 实例对象可以调用类方法，实例方法，静态方法
    > 类对象只能调用类方法和静态方法

### property属性
    > 必须返回一个值
    > 调用方法,不用（）调用
    > 参数只能传一个self
    ```
        class Good:
            @property
            def prop(self):
                return 100
                
         obj = Good()
         ret = obj.prop # 调用属性
         print(ret)
    ```
    >> 两种方法创建property属性
     >  
     >  在新式类中创建
     ```
        class Good:
        @property
        def price(self):
            print('@property')
        
        @price.setter
        def price(self. value):
            print('@price.setter')
            
        @price.delete
        def peice(self):
            print('@price.deleter') 
            
            
        g = Goods()
        g.price
        g.price = 123
        del g.price 
     ```
     > 第二种创建方式
     > property有四个参数可以接收 ipython3中help(property)
     ```
        class Foo:
            def get_bar(self):
                return '123'
                
            BAR = property(get_bar)
            
        obj = Foo()
        result = obj.BAR
        print(result)
     ```
     > python中的私有属性（就是修改私有属性名字）
### with,上下文管理
    > 实现了__enter__()和__exit__()方法的对象都可以称之为上下文管理器
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    