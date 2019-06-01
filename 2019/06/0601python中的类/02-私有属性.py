class Money(object):
    def __init__(self):
        self.__money = 100

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
            print(self.__money)
            return self.__money
        else:
            print('err，不是数字类型')

    def getMoney(self):
        return self.__money


a = Money()
ret = a.setMoney(300)
print(ret)