## Bonus challenges: Text processing

#### Word Frequencies
1. Build on the `word-count.py` code from class, but instead of providing the short string to analyse in a  variable at the top of the Python script file, work out how to load the string from a separate text file (this only requires 2-3 extra lines of code). Start with a small text file with just a paragraph or two of plain text pasted into it. Once you can see that your code is working, use a larger free ebook from [Project Gutenberg](http://www.gutenberg.org/ebooks/search/?sort_order=downloads) as your input file (make sure to download the "Plain Text UTF-8 version", **not** an HTML or ebook version).
2. (HARD!) Your new dictionary of word frequencies will now be very large, too large to print easily. You can look up the frequency of single words easily, but how will you find out what the most frequently-used words are, when the dictionary is not ordered? Hint: turn your dictionary into a list of tuples containing all the key-value pairs in your dictionary using `list(word_count.items())`, and then find out how to sort this list based on the second value in each tuple (googling required!). Now you have a large list sorted by frequency, but it's still too large to print easily. How can you print out just the 50 most frequent words? (Hint: use Python's list slice syntax.)
3. How would you filter this list to create a new list featuring ONLY words which appear more than 100 times? What about filtering out any words which are shorter than 4 characters?
---
#### Markov Chain text generator (advanced!)
1. Starting with the part of the above code which loads a text file into a single string and then into a list of words, loop through the word list and create a "Markov table" which is a dictionary where the keys are each word from the file, and each key's value is a list of all the other words which appear after that word in the original text. For example, if your input text is the string:
```python
The dogs are running. The dogs are happy. The owners are drunk. No dogs survived.```
...then your resulting Markov table might look like this:
```python
markov = {
    'The': ['dogs', 'dogs', 'owners'],
    'dogs': ['are', 'are', 'survived.'],
    'are': ['running.', 'happy.', 'drunk.'],
    'owners': ['are'],
    'running.': ['The'],
    # ...etc...
    'survived.': []
}
```
(Note that this is just an example to show you the structure - your table will be defined one key at a time in your loop, not defined all-at-once like this.)

2. Now for the text generation phase. Note the duplicates in the lists above. Your Markov table records all the words that come after any particular word in a piece of text. The more often a certain word (like 'dogs') follows a specific word (like 'The'), the more often that following word will appear in the list - and the more often it appears in the list, the more likely it is to be chosen if we randomly pick a word from that list. So: write a function `generate_text(mtable, length)` which takes your Markov table as its first argument, and a word count as a second argument. To start off the text-generation process, the function should pick a random key from the table as its starting word: then it should loop by picking a following word by choosing at random from the list of following words for that starting word. The following word then becomes the new starting word for the next iteration (i.e. we find a next following word), until you have an output string with the specified number of words in it. This output string will be different each time you run the function, due to the random selection, but overall the outputs should be in the "style" of the original text, because they have been generated following the same statistical patterns of word order as in the original text. Neat! (Note that this works best with book-length text files.)

Hint: to randomly pick a word from a list, you will need to import the right function from the `random` module:
```python
from random import choice
my_choice = choice(my_list)
```

3. How could you make sure that you always start your generated text with a word that is the start of a sentence from the original text (without cheating and just capitalizing the word yourself)?
4. How could you combine the Markov tables of two or more input texts to generate a blended-style remix of the original texts?
5. How could you change the **granularity** of your Markov table so that it keeps track not just of whole words and the words that follow them, but shorter strings of characters than words: i.e., a table of which single characters follow any N-character (i.e. 3-character) string in a text? (This will require you to loop through the input text not as a list of strings, but as one single long string of characters.) Text generated from such a table will tend to make up new words for small values of N like 2 or 3 (i.e. the characters following all 3-character strings), but start to reproduce existing words when N gets closer to the length of average words, i.e. 5 or 7.
---
Some more info on Markov chains here: https://www.youtube.com/watch?v=v4kL0OHuxXs
