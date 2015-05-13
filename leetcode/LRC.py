from collections import OrderedDict

class LRC:
    def __init__(self):
        self.cache = OrderedDict()

    def get(self):
        return self.cache.popitem(last=False)[0]

    def set(self, value):
        if value in self.cache:
            del self.cache[value]
        self.cache[value] = True



if __name__ == '__main__':
    cache = LRC()
    cache.set(3)
    cache.set(5)
    cache.set(4)
    print(cache.get())
    cache.set(5)
    print(cache.get())
    print(cache.get())