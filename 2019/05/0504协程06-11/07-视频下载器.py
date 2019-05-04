import urllib.request
import gevent
from gevent import monkey
import random

monkey.patch_all()

file_name = input('填写文件名：')
file_url = input('下载的视频网址： ')
# 'http://image.huajiao.com/6d6dde5d0873348553e29324b425c29f-150_150.jpg'

def download(url):
    req = urllib.request.urlopen(url)

    img_content = req.read()

    with open(file_name, 'wb') as f:
        f.write(img_content)

def main():
    gevent.joinall([
        gevent.spawn(download, file_url),
    ])

if __name__ == '__main__':
    main()