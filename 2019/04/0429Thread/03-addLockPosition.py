import threading
import time


g_num = 0

def test1(num):
    global g_num
    # 上锁，如果之前没有上锁，那么此时，上锁成功
    # 如果上锁之前已经被上锁，那么此时会堵塞在这里，直到这个锁解开
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print('---in test1 g_num:%d---' % g_num)
    #解锁


def test2(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print('------------------in test2 g_num:%d---'% g_num)

# create lock default no lock
mutex = threading.Lock()

def main():
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))

    t1.start()
    t2.start()

    time.sleep(8)
    print('-------------------------%d---' % g_num)


if __name__ == '__main__':
    main()