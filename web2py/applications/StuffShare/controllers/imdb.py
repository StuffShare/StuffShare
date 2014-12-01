__author__ = 'Gary Williams'

import urllib
import urllib2
import json


def get_movie_search_results():
    some_title = request.vars.some_title
    my_dict = get_movie_search_results_2(some_title)
    if my_dict:
        return dict(movie_search_results_dict=my_dict)
    else:
        return dict(movie_search_results_dict=dict()) # how should we bubble up the error?


def get_movie_search_results_2(title):
    url = 'http://www.imdb.com/xml/find?json=1&nr=1&tt=on&q=' + urllib.quote_plus(title)
    response = urllib2.urlopen(url)
    json_object = json.loads(response.read())

    result_dict = {}

    for result_group in json_object: # top level is title_substring, title_popular, title_approx, or None
        for result in json_object[result_group]:
            result_dict[result['id']] = result['title']

    return result_dict


if __name__ == "__main__":
    print get_movie_search_results_2('Shawshank')
