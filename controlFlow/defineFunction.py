# Fibonacci function example
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fib(2000)


# Assign function to a variable
print(fib)
f = fib
f(100)


# Return none value
fib(0)
print(fib(0))


# Fibonacci function return a list of numbers
def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


f100 = fib2(100)
print(f100)
