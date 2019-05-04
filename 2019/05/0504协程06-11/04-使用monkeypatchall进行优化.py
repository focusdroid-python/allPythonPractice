import gevent
import time
from gevent import monkey

monkey.patch_all()

def main1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # gevent.sleep(0.1)
        time.sleep(0.1)

def main2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.1)


def main3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.1)

g1 = gevent.spawn(main1, 5)
g2 = gevent.spawn(main2, 5)
g3 = gevent.spawn(main3, 5)

# gevent遇到延时操作，自动切换其他代码执行
g1.join()
g2.join()
g3.join()