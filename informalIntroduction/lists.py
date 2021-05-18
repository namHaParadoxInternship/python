# Overview
squares = [1, 4, 9, 16, 25]
print(squares)


# List slice/index
print(squares[0])
print(squares[-1])
print(squares[-3:])
print(squares[:])


# List concatenation
print(squares + [36, 49, 64, 81, 100])


# Change content of list
cubes = [1, 8, 27, 65, 125]
print(cubes)
cubeOfFour = 4 ** 3
print(cubeOfFour)
cubes[3] = cubeOfFour
print(cubes)


# Add new items to list
cubes.append(216)
cubes.append(7 ** 3)
print(cubes)


# Using slice to change list
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)


# List length
letters = ['a', 'b', 'c', 'd']
print(len(letters))


# Nest list
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])
