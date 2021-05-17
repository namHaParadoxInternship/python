from math import pi
from collections import deque

# Some methods of list objects
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.count('apple'))

print(fruits.count('tangerine'))

print(fruits.index('banana'))

print(fruits.index('banana', 4))

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

print(fruits.pop())

anotherList = fruits.copy()
print(anotherList)

fruits.extend(['mango', 'watermelon'])
print(fruits)

fruits.insert(3, 'melon')
print(fruits)

fruits.remove('banana')
print(fruits)

fruits.clear()
print(fruits)


# Using list as stacks
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)


# Using list as queues
queue = deque(["Eric", "John", "Michael"])
print(queue)
queue.append("Terry")
queue.append("Graham")
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)


# List of square
# original version
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

# shorter version
squares = list(map(lambda x: x**2, range(10)))
print(squares)

# much more shorter version
squares = [x**2 for x in range(10)]
print(squares)


# Finding pairs which are combinations of 2 different values from 2 different lists
# original version
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)

# shorter version
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])


# More examples
vec = [-4, -2, 0, 2, 4]

# create a new list with the values doubled
print([x*2 for x in vec])

# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])

# apply a function to all the elements
print([abs(x) for x in vec])

# call a method on each element
fruits = ['  banana', '  loganberry ', 'passion fruit  ']
print([fruit.strip() for fruit in fruits])

# create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])

# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])

# create a list with complex expressions and nested functions
print([str(round(pi, i)) for i in range(1, 6)])


# Transpose rows and columns
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# original method
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

# shorter version
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

# or using nested list comprehensions
print([[row[i] for row in matrix] for i in range(4)])

# or else using built-in function
print(list(zip(*matrix)))
