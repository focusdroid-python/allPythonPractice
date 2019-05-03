import time
from collections import Iterable
from collections import Iterator

class Classmate(object):
    def __init__(self):
        self.names = list()


    def set_name(self, name):
        self.names.append(name)


    def __iter__(self):
        """如果想让一个对象可以迭代，即可以使用for，那么必须使用__iter__方法"""
        return ClassIterator(self)

class ClassIterator(object):
    def __init__(self, obj):
        self.obj = obj
        self.current = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.current < len(self.obj.names):
            ret = self.obj.names[self.current]
            self.current += 1
            return ret
        else:
            # 数据取完之后自动调用
            raise StopIteration


classmate = Classmate()

classmate.set_name('王旭')
classmate.set_name('王二')
classmate.set_name('妹妹')
#
# print('判断是否可以迭代的对象： ', isinstance(classmate, Iterable))
#
#
# classmate_iterator = iter(classmate)
# print('判断classmate_iterator是否可以迭代器： ', isinstance(classmate_iterator, Iterator))

# print(next(classmate_iterator))
#
for name in classmate:
    print(name)
    time.sleep(0.1)