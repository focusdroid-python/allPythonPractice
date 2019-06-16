def set_fun(func):
    print('-------开始执行--------')
    def call_fun(*args, **kwargs):
        print('--------权限验证1111------')
        print('--------权限验证2222------')
        func(*args, **kwargs)
    return call_fun


@set_fun
def test(num, *args, **kwargs):
    print('-----------test1--------------%d'% num)
    print('-----------test1--------------', args)
    print('-----------test1--------------', kwargs)

test(100)
test(100, 200)
test(100, 200, 300, mm=999)
