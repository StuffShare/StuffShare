__author__ = 'Gary Williams'

import urllib2
import json

# this will return all the title matches
# for example output, see: http://www.imdb.com/xml/find?json=1&nr=1&tt=on&q=Shawshank
# we'll have to retrieve the id (e.g. tt0293927) of the appropriate match to store in our database

def find_movie_by_title(title):
    url = 'http://www.imdb.com/xml/find?json=1&nr=1&tt=on&q=' + title
    response = urllib2.urlopen(url)
    json_object = json.loads(response.read())
    return json_object
