# Simple private variable example
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method


class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


list = [[1, "honey"], [2, "sugar"], [3, "milk"]]
x = MappingSubclass(list)
for item in x.items_list:
    print(item)

numbering = [4, 5, 6]
products = ['chocolate', 'chips', 'doritos']
x.update(numbering, products)
for item in x.items_list:
    print(item)
