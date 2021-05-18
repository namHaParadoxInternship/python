# Overview
# single quotes
print('spam eggs')

# using \'
print('doesn\'t')

# using double quotes
print("doesn't")

# example 1
print('"Yes," they said.')

# example 2
print("\"Yes,\" they said.")

# example 3
print('"Isn\'t," they said.')


# Using print() with \n
print('First line.\nSecond line.')


# Using print() with 'r' letter before the quote
print(r'C:\some\name')


# Span multiple lines with print()
print("""
Usage: thingy [OPTIONS]
    -h                        Display this usage message
    -H hostname               Hostname to connect to
""")


# Strings concatenate and repeat
print(3 * 'un' + 'ium')


# Strings automatic concatenate
print('Py' 'thon')


# Break long string
print(
    'Put several strings within parentheses '
    'to have them joined together.'
)


# Concatenate variable
prefix = 'Py'
print(prefix + 'thon')


# Indexing strings
word = 'Python'
print(word[0])
print(word[5])
print(word[-1])
print(word[-2])
print(word[-6])


# Slicing strings
print(word[0:2])
print(word[2:5])


# Omit slice
print(word[:2])
print(word[4:])
print(word[-2:])


# Out of range slice index
print(word[4:42])
print(word[42:])


# Make new words out of slice
print('J' + word[1:])
print(word[:2] + 'py')


# Length of a string
str = 'ithinkthissentenceislongenoughformetouseonthistest'
print(len(str))
