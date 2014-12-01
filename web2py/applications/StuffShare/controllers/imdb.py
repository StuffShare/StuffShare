__author__ = 'Gary Williams'

import urllib
import urllib2
import json


def find_first_movie_match_by_title(title):
    url = 'http://www.omdbapi.com/?t=' + urllib.quote_plus(title) + '&y=&plot=short&r=json'
    response = urllib2.urlopen(url)
    json_object = json.loads(response.read())
    return json_object


def find_first_movie_match_by_title_and_year():
    title = request.vars.some_title
    year = request.vars.some_year
    result = find_first_movie_match_by_title_and_year_2(title, year)
    if result:
        return dict(movie_info_dict=result)
    else:
        return dict(movie_info_dict=dict()) # how should we bubble up the error?


def find_first_movie_match_by_title_and_year_2(title, year):
    url = 'http://www.omdbapi.com/?t=' + urllib.quote_plus(title) + '&y=' + year + '&plot=short&r=json'
    response = urllib2.urlopen(url)
    json_object = json.loads(response.read())
    dict_object = dict()

    dict_object['Title'] = json_object['Title']
    dict_object['Year'] = json_object['Year']

    return dict_object


def find_all_movie_matches_by_title(title):
    url = 'http://www.imdb.com/xml/find?json=1&nr=1&tt=on&q=' + urllib.quote_plus(title)
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
    print find_first_movie_match_by_title('The Shawshank Redemption')
    print ''
    print find_first_movie_match_by_title_and_year('Star Trek', '1994')
    print ''
    print get_movie_details_by_id('tt0060666')
