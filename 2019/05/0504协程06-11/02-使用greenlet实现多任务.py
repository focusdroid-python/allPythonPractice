import time
from greenlet import greenlet


def task1():
    while True:
        print('----------11111111111111-----------')
        gr2.switch()
        time.sleep(0.01)



def task2():
    while True:
        print('----------222222------------------')
        gr1 .switch()
        time.sleep(0.01)


gr1 = greenlet(task1)
gr2 = greenlet(task2)

gr1.switch()