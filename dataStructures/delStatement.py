# Some examples about using del
a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)

# delete index of a
del a[0]
print(a)

# delete slice of a
del a[2:4]
print(a)

# delete entire list of a
del a[:]
print(a)

# delete variable a
del a
print(a)