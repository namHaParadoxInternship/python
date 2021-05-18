# Simple example using finally clause
try:
    raise Exception
except:
    print('I just want to avoid the Exception for now...')
finally:
    print('Goodbye, comrade!')


# Finally clause will be executed before return no matter what
def bool_return():
    try:
        return True
    finally:
        return False

print(bool_return())