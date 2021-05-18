# Simple example about user-defined exception
class MyDefinedError(Exception):
    pass

try:
    raise MyDefinedError
except MyDefinedError:
    print('I made it good huh? :D')
    raise