import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            msg = "I'm---" + self.name + "---@---" + str(i)
            print(msg)
            self.test()

    def test(self):
        print('这是另外一个函数')

def main():
    t = MyThread()
    t.start()

if __name__ == '__main__':
    main()