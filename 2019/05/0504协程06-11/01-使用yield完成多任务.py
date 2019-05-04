import time


def task1():
    while True:
        print('-----------------------1-----------------------------')
        time.sleep(0.01)
        yield


def task2():
    while True:
        print('----------2------------------')
        time.sleep(0.01)
        yield


def main():
    t1 = task1()
    t2 = task2()
    # 先让t1运行一会儿，当t1遇到yield的时候，返回23行继续执行，然后
    # 执行t2，当遇到yield的时候，再次切换到t1
    # 这样t1/t2/t1/t2交替执行，最终实现多任务（协程的多任务就像调用函数一样简单）

    while True:
        next(t1)
        next(t2)

if __name__ == "__main__":
    main()