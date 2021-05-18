import math

# Fancier output formatting
# format with 'f' before quotation mark
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

# format with str.format()
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))


# Format values to string for debugging
s = 'Hello, world.'
print(str(s))
print(repr(s))
print(str(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

# the repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)

# the argument to repr() may be any Python object:
print(repr((x, y, ('spam', 'eggs'))))


# Formatting number
print(f'The value of pi is approximately {math.pi:.3f}.')


# Formatting minimum number of characters of a string
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')


# Add modifiers to convert values
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')


# Basic format
print('We are the {} who say "{}!"'.format('knights', 'Ni'))


# Use position of the object to pass into str.format()
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))


# Use keyword in str.format()
print('This {food} is {adjective}.'
      .format(food='spam', adjective='absolutely horrible'))


# Combine posotional and keyword arguments
print('The story of {0}, {1}, and {other}.'
      .format('Bill', 'Manfred', other='Georg'))


# Use dictionary's keywords
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))


# Use keyword-only to get value a from dictionary
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))


# Format with minimum character
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


# Manual formatting
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4))


# Using str.zfill()
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))


# Using % for number formatting
print('The value of pi is approximately %5.3f.' % math.pi)