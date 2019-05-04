import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def download(name, url):
    req = urllib.request.urlopen(url)

    img_content = req.read()

    with open(name, 'wb') as f:
        f.write(img_content)

def main():
    gevent.joinall([
        gevent.spawn(download, '1.jpg', 'http://image.huajiao.com/6d6dde5d0873348553e29324b425c29f-150_150.jpg'),
        gevent.spawn(download, '2.jpg', 'http://image.huajiao.com/b444f1616a1bcad32cce0cc39c3e8745-320_180.jpg')
    ])

if __name__ == '__main__':
    main()