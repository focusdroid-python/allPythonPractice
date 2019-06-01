class File(object):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode


    def __enter__(self):
        print('entering')
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, *args):
        print('will exit')
        self.f.close()

with File('text.html', 'w') as f:
    print('start write')
    f.write('<html><head><title>with上下文管理</title></head><body><h1>with上下文管理第二种方式</h1></body></html>')