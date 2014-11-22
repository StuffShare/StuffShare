__author__ = 'gwilliams'

import urllib2
import json

def get_book_info(isbn):
    url = 'https://openlibrary.org/api/books?jscmd=data&bibkeys=ISBN:' + isbn
    response = urllib2.urlopen(url)
    book_info = json.loads(response.read())
    return book_info

