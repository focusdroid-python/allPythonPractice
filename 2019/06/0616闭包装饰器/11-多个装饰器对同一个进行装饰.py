def add_qx(func):
    print('-------开始执行权限111--------')
    def call_fun(*args, **kwargs):
        print('--------权限验证1111------')
        return func(*args, **kwargs)
    return call_fun


def add_qxs(func):
    print('-------开始执行权限222start--------')
    def call_fun(*args, **kwargs):
        print('--------权限验证2222------')
        return func(*args, **kwargs)
    return call_fun


@add_qx
@add_qxs
def test():
    print('-----------test--------------')

test()