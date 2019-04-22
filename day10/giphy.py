# Search GIPHY and show results with title & original URL

import requests
q  = input('Enter search term:').replace(' ', '+')
URL = 'http://api.giphy.com/v1/gifs/search?q={}&api_key=dc6zaTOxFJmzC'.format(q)

results = requests.get(URL).json()
# data = res.json()

for result in results['data']:
    print('Title:', result['title'])
    print('URL: ', result['images']['original']['url'])
