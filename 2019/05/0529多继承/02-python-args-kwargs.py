def test2(a, b, *args, **kwargs):
    print('*'*50)
    print(a)
    print(b)
    print(args)
    print(kwargs)


def test(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    test2(a, b, *args, **kwargs)

test(11,22, 33,33,44,55,66, name='focusdroid', arg=12)