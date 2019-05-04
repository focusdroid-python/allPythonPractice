import gevent
from gevent import monkey
import time

monkey.patch_all()

def fn(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.1) # patch_all会将这句话修改成gevent.sleep(0.1)

gevent.joinall([
    gevent.spawn(fn, 5),
    gevent.spawn(fn, 5)
])