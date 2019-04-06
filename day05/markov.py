# Markov text generator from text file
#
# This looks long but it's mostly comments!


from random import choice  # lets us choose a random element from a list

# import urllib.request  # to open directly from URL
# data = str( urllib.request.urlopen(url).read() )

def markov_table_from_file(filename):

    # This is the preferred way to read in the data from a file
    # into a single string (it closes the file for you automatically)
    with open(filename, 'r') as file:
        data = file.read()

    words_list = data.split()  # split on whitespace into a list of words

    markov = {}  # initialise a new empty dictionary for our Markov table

    # Loop through the entire list of all the words from the file to
    # build our Markov table.
    # We want this loop to stop one short of the last word, to avoid indexing
    # beyond the end of the list when we try to access the following word
    # using 'words_list[ index + 1 ]'
    for index in range( len(words_list) - 1 ):

        word = words_list[ index ]          # get the word at the current index
        next_word = words_list[ index + 1 ] # get one word ahead

        # From this point on we don't have to use 'index' any more
        # because we used it to pull out the current and next words
        # from the word list, to store into their own variables. This
        # makes the following code more readable! Writing
        # 'next_word' is clearer than 'words_list[ index + 1 ]',
        # especially when these variables are themselves used inside
        # square brackets, as they are in the following code.

        if word in markov:
            # Append to existing list if the word already appears
            markov[ word ].append( next_word )
        else:
            # The first time we see this word as a key, initialise its
            # value to be a list containing just the next word
            markov[ word ] = [ next_word ]

        # One-liner version of the above if-elif, using get():
        #
        # markov[ word ] = markov.get(word, []) + [ next_word ]


    return markov   # After loop, return the finished dictionary


def generate_text(mtable, length):

    # Choose a random starting word to start the sentence
    word = choice( list(mtable.keys()) )

    # How could you improve this choice by making sure the starting word
    # will be capitalized? i.e. choose only a capitalized word to start,
    # not just cheating and capitalizing the words yourself.
    # Why, just keep choosing until you find a capitalised word!
    #
    word = ''
    while not word.istitle():
        word = choice( list(mtable.keys()) )

    output = ''  # Initialise our output string to be empty so we can add to it below

    for i in range(length):
        output += word + ' '  # add current word to end of output string

        # Here's how we work out what to use for the next word:
        # treat the current word as a key into our table, 'mtable[word]',
        # whose value will be the list of all the words that follow this
        # one in the text. By choosing a next word randomly from this list,
        # we get a next word with roughly the same probability as it appears
        # in the original text - because the list has duplicates, so the more
        # often the same word follows our current word, the more chance it has
        # to be randomly selected from this list. And because the input text
        # follows the rules of English(?) grammar, the generated output here is
        # statistically likely to follow those rules too, i.e. it will
        # look more or less like sensible phrases, and not just a random
        # jumble of words. Order for free! Geddit?
        word = choice( mtable[word] )

    # We could also make sure to end here with a word that ends with a
    # sentence-ending symbol
    final_word = ' '
    while final_word[-1] not in ['?', '!', '.']:
        final_word = choice( list(mtable.keys()) )
    output += final_word

    return output   # Return our finished output string


# Now to use our functions:

# Create the Markov table from a text file
# (use your own filename here)
markov = markov_table_from_file('ulysses.txt')

# Now use the resulting Markov table (dictionary)
# to create 5 new sentences of 20 words each
for i in range(5):
    new_text = generate_text(markov, 20)
    print(new_text)
