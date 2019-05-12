import re

def main():
    emailValue = input('请输入正确邮箱地址:')
    ret = re.match(r'[a-zA-Z0-9_]{4,20}@[a-zA-Z0-9]{2,10}\.com$', emailValue)
    if ret:
        print('这是正确的邮箱地址：%s,返回的结果%s' % (emailValue, ret.group()))
    else:
        print('这是不正确的邮箱地址:%s' % emailValue)

if __name__ == '__main__':
    main()