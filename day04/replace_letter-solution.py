
# Method 1: create an empty output string and add characters
# to it
#
# input_string = 'It is free to feed the geese.'
# output_string = ''
#
# for each_char in input_string:
#     # check if the current letter is 'e'
#     if each_char == 'e':
#         output_string += '_' # add '_' to the end of the output string
#     else:
#         output_string += each_char  # add the current character to the end of the output string
#
#     # print(output_string)
#
# print('output_string =', output_string)
#
# #
# # Method 2: Convert the string into a list, and replace the individual characters 'in-place'
#
# input_string = 'It is free to feed the geese.'
# string_as_list = list(input_string)
# print(string_as_list)
#
# for index, char in enumerate(string_as_list):
#     if char == 'e':
#         string_as_list[index] = '_'
#
# # print('after loop, string_as_list = ', string_as_list)
#
# output_string = ''.join(string_as_list)
#
# print('output_string =', output_string)


# Convert all vowels in the string to '_'

input_string = 'It is free to feed the geese.'
output_string = ''

for each_char in input_string:
    # # check if the current letter is 'e'
    # if each_char == 'i' or each_char == 'a' or each_char == 'e':
    #     output_string += '_' # add '_' to the end of the output string
    #
    # # elif each_char == 'e':
    # #     output_string += '_' # add '_' to the end of the output string

    if each_char in 'aeiou':
        output_string += '_' # add '_' to the end of the output string
    else:
        output_string += each_char  # add the current character to the end of the output string

    # print(output_string)

print('output_string =', output_string)

#
