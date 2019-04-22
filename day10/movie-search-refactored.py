
import themoviedb as api    # all the API functions are in their own module now
import sys    # to get command line args

# Allow search query to be given on the command line
# (join together if more than one word)
query = ' '.join( sys.argv[1:] )
# ...but if it wasn't given on command line, ask:
if not query:
    query = input('Enter search term: ')


# Perform search
results = api.search_movies(query)
results_count = len( results['results'] )

# Show error message or results
if results_count == 0:
    print("Sorry, no matches for '{}'".format(query))
    sys.exit()
else:
    print('====== Results for "{}" ========'.format(query))
    api.print_search_results(results)


# Prompt for number and show details, then prompt again
while True:

    chosen = input('\nChoose 1-{}, [enter] to print list, or (q)uit: '.format(results_count))

    if chosen.isdigit():
        # Look up the movie by its ID, and print details
        chosen = int(chosen) - 1  # Convert to int and subtract 1 to turn into index

        if chosen < 0  or  chosen > (results_count - 1):
            print('Error: invalid number: ', chosen)
            continue   # jump to top of loop and start a new iteration

        movie_id = results['results'][chosen]['id']
        movie_details = api.get_movie_details( movie_id )
        api.print_movie_details(movie_details)

    elif not chosen:
        # Show result list again if enter pressed
        api.print_search_results(results)

    elif chosen == 'q':
        break  # break out of loop, i.e. quit


print('K Bye!')
