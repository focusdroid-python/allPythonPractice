from contextlib import contextmanager


@contextmanager
def my_open(path, mode):
    f = open(path, mode)
    yield f
    f.close()


with my_open('index.html', 'w') as f:
    f.write('<html><head></head><body><h1>这是一段测试文字</h1></body></html>')