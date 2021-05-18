# Simple range
for i in range(5):
    print(i)


# Iterate over the indices of a sequence
a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print(i, a[i])


# Functions that take iterable object
print(sum(range(4)))
print(list(range(4)))