__author__ = 'Gary Williams'

import urllib2
import json

def find_movies_by_title(title):
    url = 'http://www.omdbapi.com/?t=' + title.replace(' ', '+') + '&y=&plot=short&r=json'
    response = urllib2.urlopen(url)
    json_object = json.loads(response.read())
    return json_object

def find_movies_by_title_and_year(title, year):
    url = 'http://www.omdbapi.com/?t=' + title.replace(' ', '+') + '&y=' + year + '&plot=short&r=json'
    response = urllib2.urlopen(url)
    json_object = json.loads(response.read())
    return json_object

def get_movie_details_by_id(id):
    if not (id.startswith('tt')):
        id = 'tt' + id

    url = 'http://www.omdbapi.com/?i=' + id + '&plot=short&r=json'
    response = urllib2.urlopen(url)
    json_object = json.loads(response.read())
    return json_object

if __name__ == "__main__":
    print find_movies_by_title('The Shawshank Redemption')
    print ''
    print find_movies_by_title_and_year('Star Trek', '1994')
    print ''
    print get_movie_details_by_id('tt0060666')