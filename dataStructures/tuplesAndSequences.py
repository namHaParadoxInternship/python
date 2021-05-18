# Tuple examples
t = 12345, 54321, 'hello!'
print(t[0])
print(t)

# tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)

# tuples are immutable but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)

# constructing empty tuple
empty = ()
print(len(empty))

# constructing with only 1 item
singleton = 'hello',
print(len(singleton))
print(singleton)

# unpacking tuple
x, y, z = t
print(x)
print(y)
print(z)
