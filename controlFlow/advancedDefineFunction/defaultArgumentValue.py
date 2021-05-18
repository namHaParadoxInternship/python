# Default argument value example
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


ask_ok('Hi, wanna go to next step?')

ask_ok('Yes, this is the second step (even though you not want to). Still more, do you want to proceed?', 2)

ask_ok('Here we go again! Now I\'m leaving. I swear. Say good bye?',
       2, 'Come on, only yes or no!')


# Simpler default argument value example
i = 5


def f(arg=i):
    print(arg)


i = 6
f()


# The default value is evaluated only once
def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))


# Re-assign value for variable
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))
