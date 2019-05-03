class Feibonaqie(object):
    def __init__(self, all_num):
        self.all_num = all_num
        self.a = 0
        self.b = 1
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.all_num:
            ret = self.a
            self.a, self.b = self.b, self.a+self.b
            self.current +=1
            return ret
        else:
            raise StopIteration

feibo = Feibonaqie(10000)

for num in feibo:
    print(num)
