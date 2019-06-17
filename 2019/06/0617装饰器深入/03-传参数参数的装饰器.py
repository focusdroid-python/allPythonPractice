def set_level(leve_num):
    def set_func(func):
        def call_func(*args, **kwargs):
            if leve_num == 1:
                print('---权限验证1111111-----')
            elif leve_num == 2:
                print('---权限验证2222222-----')
            return func()
        return call_func
    return set_func


@set_level(1)
def test():
    print('---------test111------')
    return 'ok'

@set_level(2)
def test2():
    print('---------test2222------')
    return 'ok'



test()
test2()