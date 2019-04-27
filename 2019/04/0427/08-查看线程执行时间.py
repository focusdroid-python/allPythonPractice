import threading
import time

def test1():
    for i in range(5):
        print('---------------------------------test1---%d--'% i)
        # time.sleep(0.0001)


def main():
    print(threading.enumerate())
    t1 = threading.Thread(target=test1)

    print(threading.enumerate())

    t1.start()

    print(threading.enumerate())

    # 当调用Thread的时候，不会创建线程
    # 当调用Thread创建出来的实例对象的start方法的时候才会调用线程以及让这个线程开始执行



if __name__ == '__main__':
    main()