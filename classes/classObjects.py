# Simple class object example
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


x = MyClass()
print(x)
print(x.i)
print(x.f())

# Simple instance object example
x.counter = 1
while x.counter < 10:
    x.counter *= 2
print(x.counter)
del x.counter


# Simple method object example
xf = x.f
print(xf())
