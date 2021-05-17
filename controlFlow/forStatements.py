# For statement
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


# For statement but more expert
# iterate over a copy
users = {
    'Nam': 'inactive',
    'Tu': 'active',
    'Dung': 'active',
    'Manh': 'inactive'
}

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print(users)

# create a new collection
users = {
    'Nam': 'inactive',
    'Tu': 'active',
    'Dung': 'active',
    'Manh': 'inactive'
}

active_users = {}

for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)
