import threading
import time

g_nums = [11, 22]

def test1(temp):
    temp.append(33)
    print('----in test1 g_num=%s---' % str(temp))

def test2(temp):
    print('-----in test2 g_num=%s-----------------------------' % str(temp))


def main():
    # args必须是一个元祖
    t1 = threading.Thread(target=test1, args=(g_nums,))
    t2 = threading.Thread(target=test2, args=(g_nums,))
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)

    print('---in Thread g_num=%s----' % g_nums)

if __name__ == '__main__':
    main()