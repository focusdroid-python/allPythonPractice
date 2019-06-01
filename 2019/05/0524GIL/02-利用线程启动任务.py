import Threading


def test():
    while True:
        pass

t1 = threading.Thread(target=test)
t1.start()

while True:
    pass
