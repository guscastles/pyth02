
# Use your own filename here
filename = 'ulysses.txt'

# This is the preferred way to read in the data from a file
# into a single string (it closes the file for you automatically)
with open(filename, 'r') as file:
    str = file.read()

words_list = str.split()  # split on whitespace into a list of words
print('Loaded', len(words_list), 'words.\n')

word_count = {}    # initialise an empty dictionary

for word in words_list:
    # if word in word_count:
    #     word_count[word] += 1
    # else:
    #     word_count[word] = 1

    # using .get() to specify a default value for a key
    word_count[word] = word_count.get(word, 0) + 1


# The frequency table will be too long to print out this way,
# and it won't be in order anyway
#
# for key, val in word_count.items():
#     print(key + ':', val)


# Time for some magic.
# It's easy to sort a list if it's just a list of numbers, using
# the builtin sorted() function.
#     my_list = [3,5,1,2]
#     sorted_list = sorted(my_list)
#
# But if we just have a list of numbers which are our frequency counts,
# we won't know which actual word each of these counts applies to. And
# yet we can't keep using a dictionary, because they are not ordered!
# What we need is a list where each element contains both the word and
# its frequency count, i.e. a list of 2-part tuples:
#
#     [
#       ('was', 341),
#       ('perfidious', 3),
#       ('the', 523),
#       ('a', 403),
#       # ...etc, not yet in frequency order!...
#     ]
#
# Luckily, this is exactly the structure that word_count.items()
# generates, so this is our input to sorted().
# BUT we need to sort this list based on that second value in each
# tuple. Luckily we can tell sorted() how to access the value which
# will be the sort key. To do this we use the 'key=function' keyword
# argument to provide a function which sorted() will run every time
# it needs to get the value to sort by: it will pass the current item
# from our list into this key function, and the function should return
# the value to sort by (no, you are not supposed to understand this).
# Then, instead of defining a function in advance we create
# a one-liner right inside the arguments to sorted() using something
# called a lamdba (an unnamed, one-line function). This is a
# fairly advanced functional programming technique, but it's still
# pretty much the simplest way to do this, so basically just trust
# that this works, and see the link for more info.
# Finally, sorted() accepts a 'reverse' keyword argument which will
# sort the list from lowest to highest value.
# https://stackoverflow.com/questions/4088265/sorted-word-frequency-count-using-python

freq_sorted = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

print('Top 30 words:')
for index in range(30):
    pair = freq_sorted[index]  # get the current tuple from the list
    print( pair[0] + ':', pair[1] )  # print word and frequency

# You can also just use Python's list slice syntax, but you won't
# get the output in one pair per line.
# print( freq_sorted[:50] )

# To filter this sorted list so it doesn't include words shorter
# than a certain length, let's create a new list and add tuples
# to it only if the word is long enough:
filtered_list = []
for pair in freq_sorted:
    if len(pair[0]) > 5:
        filtered_list.append( pair )

# OR using a "list comprehension", a shorthand way to build lists
# from other lists, with optional filtering:
# filtered_list = [ pair for pair in freq_sorted if len(pair[0]) > 5 ]

# OR using a lambda test function as an argument to filter():
# filtered_list = list(filter(lambda pair: len(pair[0]) > 5, freq_sorted))

print()
print('Top 30 words longer than 5 characters:')
print( filtered_list[:50] )
