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
    return "结束"

# 在调用create_num的时候，发现这个函数中有yield那么此时不是调用函数， 而是创建一个生成器对象focusdroid
number = int(input('请输入您想获取的斐波纳妾数列的值： '))
obj = create_num(number)

while True:
    try:
        ret = next(obj)
        print(ret)
    except Exception as ret:
        print(ret.value) # 接收上面的return中的值
        break
