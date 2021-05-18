# Simple fibonacci
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b


# print() with extra value
i = 256 * 256
print('The value of i is', i)


# Expert fibonacci
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a + b