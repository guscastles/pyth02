
import requests
from termcolor import colored  # simple coloured text in terminal!
import textwrap  # wrap text neatly to specified width
import sys  # to get command line args

# global constants
API_KEY = '24d863d54c86392e6e1df55b9a328755'
API_BASE_URL = 'https://api.themoviedb.org/3'
POSTER_BASE_URL = 'http://image.tmdb.org/t/p/w500'
IMDB_BASE_URL = 'https://www.imdb.com/title/'

# Allow search query to be given on the command line
# (join together if more than one word)
query = ' '.join( sys.argv[1:] )
# ...but if it wasn't given on command line, ask:
if not query:
    query = input('Enter search term: ')

# Construct search URL and make request
# Docs: https://developers.themoviedb.org/3/search/search-movies
SEARCH_URL = API_BASE_URL + '/search/movie?query={}&api_key={}'.format(query, API_KEY)
results = requests.get(SEARCH_URL).json()

print('====== Results for "{}" ========'.format(query))

# Loop over results and print a number, title and summary for each
for index, result in enumerate(results['results']):
    print('[{num}] {title} ({year})'.format(
      num = colored(index+1, 'green'), # red green cyan magenta yellow blue white grey
      title = colored(result['title'], 'yellow'),
      year = result['release_date'].split('-')[0])
    )
    print(result['overview'][:80] + '...')

# Get user choice and retrieve movie ID for that choice
chosen = int(input('\nChoose 1-{}: '.format(index+1))) - 1
movie_id = results['results'][chosen]['id']

# Construct URL for movie details, and make request
# Docs: https://developers.themoviedb.org/3/movies/get-movie-details
details_url = API_BASE_URL + '/movie/{}?api_key={}'.format(movie_id, API_KEY)
details = requests.get(details_url).json()

# List comprehension to pull genre strings from list of genre dictionaries
genres = [ item['name'] for item in details['genres'] ]

# These budget numbers are sometimes just given as 0 - so check first
# before trying to do the calculation, to avoid a ZeroDivisionError
if details['budget'] and details['revenue']:
    revenue_to_budget = "{:.1f}".format(details['revenue'] / details['budget'])
else:
    revenue_to_budget = 'n/a'

# Big print statement which passes the unpacked dictionary to format()
# by using '**details', allowing us to directly access the details values
# by key. But we can also add new key-value pairs to what we pass in
# to format(), which allows us to add some new data or pre-format
# some of it before it's printed.
print(
  "\n-=== Full Details ===-\n"
  "Title: {original_title}\n"
  "Tagline: '{tagline}'\n"
  "Year: {year}\n"
  "Genres: {genre_list}\n"
  "Runtime: {runtime} min\n"
  "Budget: US${budget:,}\n"
  "Revenue: US${revenue:,}\n"
  "Revenue-Budget Ratio: {revenue_to_budget}\n"
  "Poster: {poster}\n"
  "IMDB: {imdb}\n"
  "Overview:\n{overview_wrapped}\n\n".format(
    **details,
    year = details['release_date'].split('-')[0],
    genre_list = '/'.join(genres),
    revenue_to_budget = revenue_to_budget,
    poster = POSTER_BASE_URL + details['poster_path'],
    imdb = IMDB_BASE_URL + details['imdb_id'],
    overview_wrapped = textwrap.fill(details['overview'], 60)
))
