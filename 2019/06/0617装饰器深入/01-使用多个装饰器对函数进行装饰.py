def add_qx(func):
    print('------开始进行装饰权限111功能')
    def call_func(*args, **kwargs):
        print('--------这是权限11111----')
        return func(*args, **kwargs)
    return call_func

def add_xx(func):
    print('------开始进行装饰权限222功能')
    def call_func(*args, **kwargs):
        print('--------这是权限222----')
        return func(*args, **kwargs)
    return call_func


@add_qx
@add_xx
def test():
    print('------test------')


test()