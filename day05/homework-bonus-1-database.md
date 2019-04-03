### Build a database!

Use a nested dictionary to create a database of movies, books, albums,
or whatever you want, with appropriate fields for each item.

Here's an example of the structure. Your top-level keys should be
related to the title of the item to make it easy to lookup (in reality, this key would probably be a unique ID like an ISBN barcode number):

```python
# Books database
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
        'pages': 400,
        'genres': ['science fiction', 'utopian', 'anti-authoritarian']
    }
    # ...etc...
}
```

Create functions to let a user:

1. Lookup an item by the top level key (which we'll call the ID) and print out a formatted entry of all the fields for the record found, e.g. `find_by_id(db, 'ulysses')`. A polite error message should be printed if the key does not exist.
2. Search for an item by the value of a specific fields, e.g. `find_by_field(db, 'year', 1984)`. It should print the details of any record that matches. Bonus: allow substring matches for string values.
3. Add a new item by passing in the key-value pairs as keyword arguments, e.g.
`create_record(db, 'debt', full_title='Debt: The First 5,000 Years', author='David Graeber', ...etc...)`. Your function should give an error if a record with the same ID (top-level key) already exists!
