__author__ = 'gwilliams'

import urllib2
import json

ISBNDB_ACCOUNT_NUMBER = 'I7G9FT9U' # this account number is good for 500 queries per day

def get_book_info(isbn):
    url = 'http://isbndb.com/api/v2/json/' + ISBNDB_ACCOUNT_NUMBER + '/book/' + isbn
    response = urllib2.urlopen(url)
    book_info = json.loads(response.read())
    return book_info

def get_book_title(isbn):
	book_info = get_book_info(isbn)

	# the following statement assumes the isbn was found.
	# we should probably test for error conditions.
	return book_info['data'][0]['title_latin']

# isbndb returns a json object like the following in the event of an error:
#{
#   "error" : "Unable to locate 0735619679"
#}