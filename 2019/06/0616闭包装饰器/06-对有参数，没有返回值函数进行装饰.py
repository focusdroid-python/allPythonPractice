def set_fun(func):
    def call_fun(num):
        print('--------权限验证1111------')
        print('--------权限验证2222------')
        func(num)
    return call_fun



@set_fun
def test(num):
    print('-----------test1-->: %d-------------'% num)

test(100)
test(800)