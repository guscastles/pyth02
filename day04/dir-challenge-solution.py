
def dirs(obj):
    # First, we use the original dir() function to get
    # the list of method names for the object passed in, i.e.
    # we just 'forward' the obj argument received by our dirs()
    # function straight in to dir()
    methods = dir(obj)

    # To turn the resulting list of strings into a single string,
    # we use the join() method, first specifying the separator string
    # to use in between each of our strings:
    string_result = ' '.join(methods)

    # Now just return this new string from our function
    return string_result

print("dirs('a string'):")
print( dirs('a string') )

# We can rewrite the above without using temporary local
# variables, and by calling functions inside the parentheses
# of other function calls. The result is a bit less readable,
# but it's a nice short one-liner:
def dirs_short(obj):
    return ' '.join(dir(obj))

print("dirs_short('a string'):")
print( dirs_short('a string') )



def dirs_filtered(obj):

    methods = dir(obj)

    # To filter out methods starting with '__', let's
    # construct a new output string, and use a for loop to
    # iterate over the list of methods, only adding to our
    # output string the methods that don't start with underscores

    output_string = ''

    for method in methods:
        if not method.startswith('__'):
            output_string += method + ' '

    # We add a space after adding each method name to our output
    # string, to keep them separated from each other.
    # But otice that we're going to have an extra space character
    # after our last method name. It's not really a problem here,
    # but it might be, in a more strict scenario.
    # To avoid that, we could construct an output list instead of
    # a string, and use join() to turn it into a string just before
    # we return it (join() won't add the separator string after
    # the last element).

    return output_string

print("dirs_filtered('a string'):")
print( dirs_filtered('a string') )


# ADVANCED: The above task of looping through a list and creating
# a new list from its elements, while filtering out some items,
# is such a common programming task that Python has a construct
# called a "list comprehension" that lets us do this in one line.

def dirs_filtered_list_comprehension(obj):
    # use a list comprehension to quickly filter the list into a new one:
    method_list = [method for method in dir(obj) if not method.startswith('__')]

    # create a string from the list and return it:
    return ' '.join(method_list)

print("dirs_filtered_list_comprehension('a string'):")
print( dirs_filtered_list_comprehension('a string') )
