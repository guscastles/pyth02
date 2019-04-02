
str = "the quick brown fox saw the other fox the end"

# 1. turn the string into a list of words
# 2. loop through the list and add each word as a key
#    to a dictionary - with a value of 1 if it's the
#    first occurrence of the word, otherwise the value
#    should indicate how many times that word has appeared
# 3. Print out a report with the final count of occurences
#    for each word

words_list = str.split()

word_count = {}

for word in words_list:
    # if word in word_count:
    #     word_count[word] += 1
    # else:
    #     word_count[word] = 1

    # using .get() to specify a default value for a key
    word_count[word] = word_count.get(word, 0) + 1

for key, val in word_count.items():
    print(key + ':', val)
