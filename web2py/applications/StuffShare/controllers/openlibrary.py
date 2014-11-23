__author__ = 'gwilliams'

import urllib2
import json

def get_book_info(isbn):
    url = 'https://openlibrary.org/api/books?jscmd=data&bibkeys=ISBN:' + isbn
    response = urllib2.urlopen(url)
    json_object = json.loads(response.read())
    return json_object

def get_book_title(isbn):
    book_info = get_book_info(isbn)
    return book_info['title']
