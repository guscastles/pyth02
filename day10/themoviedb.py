
import requests
from termcolor import colored  # simple coloured text in terminal!
import textwrap  # wrap text neatly to specified width

# global constants
API_KEY = '24d863d54c86392e6e1df55b9a328755'
API_BASE_URL = 'https://api.themoviedb.org/3'
POSTER_BASE_URL = 'http://image.tmdb.org/t/p/w500'
IMDB_BASE_URL = 'https://www.imdb.com/title/'


def search_movies(query):
    """Given a text query, construct API search URL and preform request, returning the results."""

    search_path = '/search/movie?query={}&api_key={}'.format(query, API_KEY)
    search_url = API_BASE_URL + search_path

    return requests.get(search_url).json()


def print_search_results(results):
    """"Print out formatted search results, with index number, for the API results dictionary passed in. """

    for index, result in enumerate(results['results']):

        print('[{num}] {title} ({year})'.format(
          num   = colored(index+1, 'green'),
          title = colored(result['title'], 'yellow'),
          year  = result['release_date'].split('-')[0])
        )
        print(result['overview'][:80] + '...')


def get_movie_details(id):
    """Get movie by themoviedb ID from API and return results."""

    details_url = API_BASE_URL + '/movie/{}?api_key={}'.format(id, API_KEY)
    return requests.get(details_url).json()


def print_movie_details(movie):
    """Print out details for the given movie. Includes genres, formatted budget figures,
    poster and IMDB URLs."""

    # List comprehension to pull genre strings from list of genre dictionaries
    genres = [ item['name'] for item in movie['genres'] ]

    # These numbers are sometimes just given as 0 - so check first
    # before trying to do the calculation, to avoid a ZeroDivisionError
    if movie['budget'] and movie['revenue']:
        revenue_to_budget = "{:.1f}".format(movie['revenue'] / movie['budget'])
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
        **movie,
        year = movie['release_date'].split('-')[0], # get just the year
        genre_list = ', '.join(genres),
        revenue_to_budget = revenue_to_budget,
        poster = POSTER_BASE_URL + movie['poster_path'],
        imdb = IMDB_BASE_URL + movie['imdb_id'],
        overview_wrapped = textwrap.fill(movie['overview'], 60)  # wrap at 60 chars!
    ))
