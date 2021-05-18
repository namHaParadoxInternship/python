# Simple class and instance variables example
class Dog:

    kind = 'canine'
    toys = []

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

    def add_toy(self, toy):
        self.toys.append(toy)


d = Dog('Fido')
print(d.kind)
print(d.name)

e = Dog('Buddy')
print(e.kind)
print(e.name)

# class variable will be shared for all Dog instance
d.add_toy('running mice')
e.add_toy('dognip')
print(d.toys)

# instance variable will stay for only 1 instance object
d.add_trick('roll over')
print(d.tricks)

e.add_trick('play dead')
print(e.tricks)
