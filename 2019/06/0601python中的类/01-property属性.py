class Goods:
    @property
    def size(self):
        return 200


g = Goods()
ret = g.size
print(ret)