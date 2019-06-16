def set_fun(func):
    print('-------开始执行--------')
    def call_fun():
        print('--------权限验证1111------')
        func()
        print('--------权限验证2222------')
    return call_fun


@set_fun
def test():
    print('-----------test1--------------')

# test()