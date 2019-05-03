def create_num(all_num):
    a, b = 0,1
    current = 0

    while current < all_num:
        # print(a)
        # 如果一个函数中有yield语句， 那么这个不是一个函数，而是一个生成器模板
        ret = yield a
        print('>>>>>ret>>>>> ', ret)
        a, b = b, a+b
        current += 1


# 在调用create_num的时候，发现这个函数中有yield那么此时不是调用函数， 而是创建一个生成器对象focusdroid
# number = int(input('请输入您想获取的斐波纳妾数列的值： '))
obj = create_num(10)


ret = next(obj)
print(ret)

ret = obj.send('ok') # 不能放在第一行
print(ret)
ret = obj.send('ok')
print(ret)
ret = obj.send('ok')
print(ret)


