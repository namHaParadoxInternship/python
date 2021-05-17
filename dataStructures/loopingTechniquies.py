# Looping through a dictionary
import math
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# Looping through a sequence
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# Pair values with zip() function when looping through 2 or more sequences
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# Loop over a sequence in reverse
for i in reversed(range(1, 10, 2)):
    print(i)

# Loop over a sequence in sorted order
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

# Loop over a sequence and ignore duplicate elements
for f in sorted(set(basket)):
    print(f)

# A very safe way looping to avoid changing the sequence
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)
