def set_fun(func):
    def call_fun():
        print('--------权限验证1111------')
        func()
        print('--------权限验证2222------')
    return call_fun


def veril(func):
    def versils():
        print('------验证规则111111111111111111111111111------')
        func()
        print('------验证规则222222222222222222222222------')
    return versils

@veril
@set_fun
def test():
    print('-----------test1--------------')

test()