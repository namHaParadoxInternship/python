# Simple example about raising an exception
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise