__author__ = 'Gary Williams'

import urllib2
import json
import amazon

ISBNDB_ACCOUNT_NUMBER = 'I7G9FT9U' # this account number is good for 500 queries per day

def get_book_info(some_isbn):
    if not amazon.is_valid_isbn(some_isbn):
        return some_isbn + " is not a valid ISBN"

    isbn10, isbn13 = amazon.fix_isbn(some_isbn)

    url = 'http://isbndb.com/api/v2/json/' + ISBNDB_ACCOUNT_NUMBER + '/book/' + isbn13
    response = urllib2.urlopen(url)
    book_info = json.loads(response.read())
    return book_info


def get_book_title(some_isbn):
    if not amazon.is_valid_isbn(some_isbn):
        return some_isbn + " is not a valid ISBN"

    isbn10, isbn13 = amazon.fix_isbn(some_isbn)

    book_info = get_book_info(isbn13)

    # the following statement assumes the isbn was found.
    # we should probably test for error conditions.
    return book_info['data'][0]['title_latin']


if __name__ == "__main__":
    CC2_ISBN_13 = '9780735619678'

    print get_book_title(CC2_ISBN_13)

# isbndb returns a json object like the following in the event of an error:
#{
#   "error" : "Unable to locate 0735619679"
#}