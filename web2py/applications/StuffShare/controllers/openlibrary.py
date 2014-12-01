__author__ = 'Gary Williams'

import urllib2
import json
import amazon

def get_book_info(some_isbn):
    if not amazon.is_valid_isbn(some_isbn):
        return some_isbn + " is not a valid ISBN"

    isbn10, isbn13 = isbn.fix_isbn(some_isbn)

    url = 'https://openlibrary.org/api/books?jscmd=data&bibkeys=ISBN:' + isbn10
    response = urllib2.urlopen(url)
    json_object = json.loads(response.read())
    return json_object

def get_book_title(isbn):
    if not amazon.is_valid_isbn(some_isbn):
        return some_isbn + " is not a valid ISBN"

    isbn10, isbn13 = isbn.fix_isbn(some_isbn)

    book_info = get_book_info(isbn10)
    return book_info['title']
