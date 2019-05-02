import multiprocessing
import time

def download_from_web(q):
    data = list(range(100))
    for temp in data:
        q.put(temp)
    print('下载器已经下载完毕！')


def share_data(q):
    '''数据处理'''
    time.sleep(5)
    waitting_data = list()
    print('读数据')
    while True:
        data = q.get()
        waitting_data.append(data)
        if q.empty():
            return
    print(waitting_data)



def main():
    # 1. 创建一个队列
    q = multiprocessing.Queue()

    # 2. 创建多个线程，将队列的引用做参数传递到里面
    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=share_data, args=(q,))

    p1.start()
    p2.start()

if __name__ == '__main__':
    main()