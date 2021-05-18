# Simple example about binding exception instance to a variable
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    # the exception instance
    print(type(inst))
    # arguments stored in .args
    print(inst.args)
    # __str__ allows args to be printed directly,
    print(inst)
    # unpack args
    x, y = inst.args
    print('x =', x)
    print('y =', y)
