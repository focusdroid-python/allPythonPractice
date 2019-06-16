import time


def set_fun(func):
    def call_fun():
        start_time = time.time()
        func()
        end_time = time.time()
        print('--------%f' % (end_time - start_time))
    return call_fun



@set_fun
def test():
    print('-----------test1-------------')

test()
test()
test()