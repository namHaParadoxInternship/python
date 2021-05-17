# There're no duplicated values in set
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)


# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')

# unique letters in a and b separately
print(a)
print(b)

# letters in a but not in b
print(a - b)

# letters in a or b or both
print(a | b)

# letters in both a and b
print(a & b)

# letters in a or b but not both
print(a ^ b)


# Set comprehension
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
