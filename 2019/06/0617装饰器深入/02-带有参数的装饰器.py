def set_func(func):
    def call_func(*args, **kwargs):
        print('---权限验证1111111-----')
        return func()
    return call_func


@set_func
def test():
    print('---------test111------')
    return 'ok'

@set_func
def test2():
    print('---------test2222------')
    return 'ok'



test()