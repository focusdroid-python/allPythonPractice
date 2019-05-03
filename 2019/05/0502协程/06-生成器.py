def create_num(all_num):
    a, b = 0,1
    current = 0
    print('---start--')

    while current < all_num:
        # print(a)
        # 如果一个函数中有yield语句， 那么这个不是一个函数，而是一个生成器模板
        yield a
        a, b = b, a+b
        current += 1
    print('---end---')

# 在调用create_num的时候，发现这个函数中有yield那么此时不是调用函数， 而是创建一个生成器对象focusdroid
obj = create_num(10)

for num in obj:
    print(num)