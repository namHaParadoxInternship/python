# Prime number finder with for-else and break statement
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')


# Odd number finder with continue statement
for num in range(2, 10):
    if num % 3 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)
