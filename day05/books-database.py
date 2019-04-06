# Books Database
#
# There's a lot of code here! Remember that in Atom you can type
# cmd + k and then cmd + 1 to collapse or 'fold up' all the bodies
# of functions, loops, dictionaries etc and just see the outline.
# Then you can click on the '...' or the line number to expand or unfold
 # and see the details!
#
# I have added a menu system here but that was not part of the homework.


# Our main database, a nested dictionary
db = {
    'ulysses': {
        'full_title': 'Ulysses',
        'author': 'James Joyce',
        'publisher': 'Sylvia Beach',
        'year': 1922,
        'pages': 900,
        'genres': ['modernism', 'experimental', 'smut']
    },
    'dispossessed': {
        'full_title': 'The Dispossessed',
        'author': 'Ursula Le Guin',
        'publisher': 'Harper & Row',
        'year': 1974,
        'pages': 390,
        'genres': ['science fiction', 'utopian', 'anti-authoritarian']
    },
    'peripheral': {
        'full_title': 'The Peripheral',
        'author': 'William Gibson',
        'publisher': 'Penguin',
        'year': 2015,
        'pages': 390,
        'genres': ['science fiction', 'speculative', 'time travel']
    },
    'neuromancer': {
        'full_title': 'Neuromancer',
        'author': 'William Gibson',
        'publisher': 'Penguin',
        'year': 1984,
        'pages': 500,
        'genres': ['science fiction', 'cyberpunk', 'hacker']
    },
    'outline': {
        'full_title': 'Outline',
        'author': 'Rachel Cusk',
        'publisher': 'Faber & Faber',
        'year': 2015,
        'pages': 256,
        'genres': ['fiction', 'autobiographical', 'memoir', 'contemporary']
    }
}

# This is a 'schema' of the database, a list of the valid keys for a book entry.
# We'll use it when adding or editing a book, so we'll know exactly which fields
# should be filled out (i.e. don't just assume that any one entry in the DB has
# all the correct fields)
db_book_fields = ['full_title', 'author', 'publisher', 'year', 'pages', 'genres']


# Here are all the functions we will use in this database program:

def main_menu():
    # Multi-line strings in Python! Start with """ (three double-quotes)
    # and end with """
    print("""
    Main Menu
    ---------

    (1) Lookup book by ID
    (2) Search for book by field value
    (3) Add a new book

    (x) Exit

    """)

    # TODO: Add the 'Edit book' feature your damn self!

    choice = input("Please enter a number or 'x': ")
    print()

    # How could you use a dictionary here instead of the if-elif chain?
    if choice == '1':
        menu_book_lookup()
    elif choice == '2':
        menu_book_search_fields()
    elif choice == '3':
        menu_book_add()
    elif choice != 'x':
        # any other input besides the numbers or 'x' is invalid
        print('Invalid option:', choice)
        print()

    # return the user input so the main while loop knows if it should exit
    return choice



def menu_book_lookup():
    """Asks the user for book ID and does lookup via book_find_by_id()"""
    # ^ This is a 'docstring', it documents the function's behaviour
    # You can see how it's used by running help(menu_book_lookup) in IPython
    # More info here: https://www.python.org/dev/peps/pep-0257/


    print('Lookup book by ID')
    search_id = input('Please enter book ID (enter to see all IDs): ')

    # Help the user out by printing out all valid IDs (keys of the db dictionary)
    # if they just hit enter without typing anything, which causes input() to
    # return an empty string.
    # Printing out all the IDs would obviously not be practical for a more
    # realistic (larger) database.
    while search_id == '':
        print( 'Book IDs in system:\n  ' + '\n  '.join(db.keys()), '\n' )
        search_id = input('Please enter book ID (enter to see all IDs): ')

    # Use another function whose job is JUST to lookup the book in the specified
    # ID, and return the dictionary for that book - or None if it can't find the book.
    # The function also prints an error message if no book was found.
    # TODO: does this function really need to exist? We could replace it with
    # 'book = db.get(search_id, None)' and print an error as part as an 'else' clause
    # below.
    book = book_find_by_id(db, search_id)

    # Then we pass this result into another function whose job is JUST to nicely print
    # out the details for a specific book (a dictionary) - but only if a valid book
    # (i.e. something truthy) was returned from the find function (i.e., not None)
    if book:
        print_book(book)


def book_find_by_id(database, id):
    """ Look up book by ID in specified database dictionary.

    Returns the book's dictionary, or None if no book is found.
    Also prints an error message if book is not found.
    """

    if id in database:
        # Easy! The book exists, just return the value of that key
        return database[id]
    else:
        print("Sorry! No book with this ID exists:", id)
        return None  # Functions return None by default, but better to be explicit here




def menu_book_search_fields():
    """Asks the user for string and searches all fields of all books, printing all matches."""

    print('Search books by field value')
    search_string = input('Please enter a search string: ')

    # Use a function which just returns a list of matching books.
    # Notice I'm passing in the 'db' and 'db_book_fields' variables, even though
    # they're global variables and I *could* just refer to them directly in the
    # function body. But by passing these variables to the function as arguments
    # instead of just assuming they've been defined globally, the function
    # becomes more flexible and generic, more independent of the variables
    # defined elsewhere in the program, easier to test, etc.
    results = book_find_by_field_value(db, db_book_fields, search_string)

    # Then loop through this list and re-use our book printing function
    # print each one (or give a message if no books were returned, i.e.
    # the results list is empty, i.e. falsey)
    if results:
        print("\nFound", len(results), "results for '" + search_string + "':")
        for book in results:
            print_book(book)
        print()
    else:
        print('\nSorry! Your search found no matches.\n')


def book_find_by_field_value(db, fields_to_search, string):
    """Returns a list of all books for which any of the specified fields match the given string.

    Returns an empty list if no matches are found.
    """

    matches = []

    # Loop through every book
    for book in db.values():
        # For each book, loop through every field
        for field in fields_to_search:
            # Let's use another function here to check whether our string appears in the field.
            # It's worth writing a function to do this, because there'a a few different kinds
            # of checking to do, for different field types: there are strings, integers and
            # lists to be checked, so we should check for all those types and treat them
            # differently! (Just testing for 'string in value' or 'string == value' won't work!)
            if appears_in_field(book[field], string):
                matches.append( book )

    return matches


def appears_in_field(field_value, string):
    """Tests a value for a string and returns True or False. Handles string, integer and list value types."""

    # The preferred way to test types is to use the built-in function isinstance():
    #     if isinstance(field_value, str)
    # but I'm going to use this version because it's a bit clearer for now:

    if type(field_value) == str:
        # Case-insensitive search by converting both to lowercase.
        # Then we just use 'in' to check for whole- or sub-string match!
        return string.lower() in field_value.lower()

    elif type(field_value) == int:
        # If it's a number field (like date or year), convert to a string first
        return string.lower() in str(field_value)

    elif type(field_value) == list:
        # This is just for checking the list of genres, a special case.
        # We should loop through each item in the list and do a substring check, because
        # if we were to just write 'str in field_value' we would only get
        # a match on exact genre name strings, not substrings.
        for item in field_value:
            if string in item:
                return True

        return False    # this means we found no substring matches during the loop

    else:
        # Catch-all, default false for any other field types
        return False


def menu_book_add():
    """Prompts user for fields of new book and adds to database dictionary"""

    print('Add New Book')
    id = input('Enter ID (key) for book: ')

    # Use our db_book_fields list to prompt for the rest of the fields
    # in a loop, adding to a new dictionary

    new_book = {}

    for key in db_book_fields:
        # Create printable version of field name for input prompt
        field_printable = key.replace('_', ' ').title()
        # Get user input and add key & value to new_book
        new_book[key] = input(field_printable + ': ')

        # Genres are a special case! We should split the input string on
        # commas to make a list of genre strings
        # TODO: Instruct the user to enter the genres this way!
        if key == 'genres':
            new_book[key] = new_book[key].split(', ')

    # Add new book to our main database
    db[id] = new_book

    # Confirm for user by printing out new book details
    print()
    print('Done! Added the following new book:')
    print_book( db[id] )



def print_book(book):
    """Prints the details for a single book"""

    print()
    print('===========================')

    # Use a for loop to go through each key-value pair.
    # Let's use the db_book_fields list to do this, so we print
    # the fields in the preferred order (i.e. full title first!)
    # otherwise we'll get the fields in whatever order the dictionary
    # has decided on.
    for key in db_book_fields:

        # Only print the field if it exists for this particular book!
        if key in book:

            # Use the key as the field title but replace underscores with
            # spaces, and capitalize words
            field_printable = key.replace('_', ' ').title()
            print(field_printable + ':', book[key])

            # TODO: the list of genres prints out as a piece of code.
            # How would you check in this loop if you're dealing with a list for
            # the value of the current field, and print it out in a more
            # human-readable way?

    print('===========================')
    print()



# Main program loop: show the main menu, get choice from the user,
# and run the corresponding function

menu_choice = ''

while menu_choice != 'x':
    # print main menu, run appropriate function,
    # and get user choice so we know when to quit
    menu_choice = main_menu()


# We're out of the main while loop, so it must be time to quit
print('Goodbye!')
