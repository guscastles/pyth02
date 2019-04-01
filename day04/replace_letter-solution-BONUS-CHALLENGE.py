
def replace_letters(input, letters_to_replace, replacement='_'):

    # To check the arguments received by this function:
    # print('--------------------------')
    # print('input:', input)
    # print('letters_to_replace:', letters_to_replace)
    # print('replacement:', replacement)
    # print('--------------------------')

    # Or, more briefly, using the builtin vars() function
    # which returns a dictionary of local variables:
    # print('arguments:', vars())

    output_string = ''

    for each_char in input:
        if each_char in letters_to_replace:
            output_string += replacement
        else:
            output_string += each_char

    return output_string


# Second version, taking multiple arguments for letters to replace,
# and also an optional error flag which changes the return value.
# Note that the actual test for whether to replace the current
# character doesn't actually change for this version of the function.
# This is because the 'in' operator is so versatile: we can test for
# the presence of the character in a list, string or tuple using
# exactly the same code.
def replace_letters_args(input, *letters_to_replace, replacement='_', error_on_fail=False):

    output_string = ''
    replaced_count = 0

    for each_char in input:
        if each_char in letters_to_replace:
            output_string += replacement
            replaced_count += 1
        else:
            output_string += each_char

    # Check whether to handle errors more loudly,
    # based on the last optional argument
    if error_on_fail and replaced_count == 0:
        print("Error: no matches!")
        return ''   # early return!

    # This line does not need to be inside an 'else'
    # attached to the condition above... can you see why?
    return output_string

    # We will never reach this line because of the 'return'
    # statement above... but if you wanted to return both
    # the new string AND the number of characters replaced,
    # just return a list (or tuple) from this function
    # (of course, the code that calls this function will need
    # to expect to have a list returned):
    return [output_string, replaced_count]



# Tests for replace_letters()

print()
print('TEST: Single character to replace, replacement specified')
print("function call  : replace_letters('feed the geese', 'e', 'X')")
print('expected output: fXXd thX gXXsX')
print('actual output  :', replace_letters('feed the geese', 'e', 'X'))
print('=========================')

print('TEST: List of characters to replace, omit replacement character i.e. use default')
print("call: replace_letters('feed the geese', ['e', 't'])")
print('expected output: f__d _h_ g__s_')
print('actual output  :', replace_letters('feed the geese', ['e', 't']))
print('=========================')

print('TEST: String of characters to replace, omit replacement character i.e. use default')
print("call: replace_letters('feed the geese', 'eg')")
print('expected output: f__d th_ ___s_')
print('actual output  :', replace_letters('feed the geese', 'eg'))
print('=========================')

print('TEST: Specify replacement character as keyword argument')
print("call: replace_letters('feed the geese', 'eg', replacement='X')")
print('expected output: fXXd thX XXXsX')
print('actual output  :', replace_letters('feed the geese', 'eg', replacement='X'))
print('=========================')


# Tests for replace_letters_args()

# NOTE: since the characters to be replaced are now specified as an
# unknown-in-advance number of arguments, trying to specify
# the replacement character as a normal positional argument will
# no longer work: it will just be treated as another character to be
# replaced, and you will get the default value for the replacement
# character. To force python to recognise the final argument as
# the replacement character, you must make it unambiguous by
# specifying it as a keyword arg: replacement='X'.
print('TEST: Multiple args to replace, replacement character as keyword argument')
print("call: replace_letters_args('feed the geese', 'e', 't', replacement='X')")
print('expected output: fXXd XhX gXXsX')
print('actual output  :', replace_letters_args('feed the geese', 'e', 't', replacement='X'))
print('=========================')

print('TEST: Error handling argument')
print("call: replace_letters_args('feed the geese', 'x', replacement='.', error_on_fail=True)")
print('expected output: "" (empty string, with error printed)')
print('actual output  :', replace_letters_args('feed the geese', 'x', replacement='.', error_on_fail=True))
print()

# FINALLY: Notice that right now the tests above force you to check manually, by looking,
# whether the expected output matches the actual output. But since our function returns
# a string, why can't we write some code to check whether this string is what we expect?
# Answer: we can, and should! You can write this test using a simple if statement
# which prints an error if the strings don't match... but since this is such a common
# task, there is a builtin statement called 'assert' which makes it easy to do this!
#
# See here for more info: https://www.programiz.com/python-programming/assert-statement
