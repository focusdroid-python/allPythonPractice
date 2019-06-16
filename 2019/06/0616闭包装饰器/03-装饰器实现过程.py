# 装饰器实现过程

def set_fun(func):
    def call_fun():
        print('------权限验证111----')
        print('------权限验证222----')
        func()
    return call_fun



def test():
    print('-----------test1-------------')

ret = set_fun(test)
ret()
print(ret)

