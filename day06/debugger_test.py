
def first(aa):
    print('in first()')
    second(aa)
    print('back from second(), end of first()')
    return 'first return'

def second(bb):
    print('in second()')
    third(bb)
    print('back from third(), at end of second()')
    return 'second return'

def third(cc):
    print('in third(), arg=', cc)
    local_var = cc
    # can you change the value of local_var in the debugger before it prints?
    print('at end of third(), local_var=', local_var)
    return 'third return'


import ipdb; ipdb.set_trace()
# start the chain of function calls
result = first(11)
print(result)
