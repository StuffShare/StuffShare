__author__ = 'Gary Williams'

import base64
import hmac
import urlparse
import time
import urllib2
import re
import isbn

from hashlib import sha256 as sha256
from xml.etree import ElementTree as ET

AWS_ACCESS_KEY_ID = 'AKIAJSUR6X4TI3SSLYZA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_ASSOCIATE_ID = 'sc4p-20'

# adapted from http://www.princesspolymath.com/princess_polymath/?p=182
def get_signed_url(params):
    action = 'GET'
    server = "webservices.amazon.com"
    path = "/onca/xml"

    params['Version'] = '2009-11-02'
    params['AWSAccessKeyId'] = AWS_ACCESS_KEY_ID
    params['Service'] = 'AWSECommerceService'
    params['Timestamp'] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    # quote and sort the parameter-value pairs
    key_values = [(urllib2.quote(k), urllib2.quote(v)) for k, v in params.items()]
    key_values.sort()

    # combine parameter-value pairs into a query string
    paramstring = '&'.join(['%s=%s' % (k, v) for k, v in key_values])

    # attach parameter-value pairs to the URL
    url = "http://" + server + path + "?" + ('&'.join(['%s=%s' % (k, v) for k, v in key_values]))

    # sign the request and attach the signature to the URL
    str = action + "\n" + server + "\n" + path + "\n" + paramstring
    my_hmac = hmac.new(AWS_SECRET_ACCESS_KEY, str, digestmod=sha256)
    url = url + "&Signature=" + urllib2.quote(base64.encodestring(my_hmac.digest()).strip())

    return url


# borrowed from http://stackoverflow.com/questions/9986179/
def http_get(url):
    while True:
        try:
            response = urllib2.urlopen(url)
            return response
        except urllib2.HTTPError, detail:
            if detail.errno == 500:
                time.sleep(1)
                continue
            else:
                raise


def get_book_info_as_xml(some_isbn):
    isbn10, isbn13 = isbn.fix_isbn(some_isbn)

    print 'requesting ' + isbn10 + '...'

    params = {'ResponseGroup': 'ItemAttributes,Images',
              'AssociateTag': AWS_ASSOCIATE_ID,
              'Operation': 'ItemLookup',
              'SearchIndex': 'Books',
              'IdType': 'ISBN',
              'ItemId': isbn10}
    url = get_signed_url(params)

    response = http_get(url)
    xml_string = response.read()

    # remove the obnoxious namespace
    xml_string = re.sub(' xmlns="[^"]+"', '', xml_string, count=1)

    # construct the xml object
    xml_object = ET.fromstring(xml_string)

    # remove the useless 'OperationRequest' node
    operationRequest = xml_object.find('OperationRequest')
    xml_object.remove(operationRequest)

    items = xml_object.find('Items')

    request = items.find('Request')
    items.remove(request)

    copy_of_item_list = items.findall('Item')

    for item in copy_of_item_list:
        asin = item.find('ASIN')
        print 'found item ' + asin.text

        if asin.text == isbn10:
            # remove the 'ItemLinks' node
            itemLinks = item.find('ItemLinks')
            item.remove(itemLinks)
        else:
            print "removing item " + asin.text
            items.remove(item)

    return xml_object


def get_book_info_as_dict():
    some_isbn = request.vars.some_isbn
    return dict(book_info_dict=get_book_info_as_dict(some_isbn))


def get_book_info_as_dict(some_isbn):
    isbn10, isbn13 = isbn.fix_isbn(some_isbn)

    root = get_book_info_as_xml(isbn10)
    item = root.find('Items/Item')
    attributes = item.find('ItemAttributes')
    book_info_dict = dict()

    book_info_dict['Title'] = attributes.find('Title').text
    book_info_dict['Author'] = attributes.find('Author').text
    book_info_dict['Publisher'] = attributes.find('Publisher').text
    book_info_dict['PublicationDate'] = attributes.find('PublicationDate').text
    book_info_dict['SmallImage'] = item.find('SmallImage/URL').text
    book_info_dict['MediumImage'] = item.find('MediumImage/URL').text
    book_info_dict['LargeImage'] = item.find('LargeImage/URL').text
    book_info_dict['ISBN-10'] = isbn10
    book_info_dict['ISBN-13'] = isbn13
    return book_info_dict


def get_book_title(some_isbn):
    dict = get_book_info_as_dict(some_isbn)
    return dict['Title']


def get_book_small_image(some_isbn):
    dict = get_book_info_as_dict(some_isbn)
    return dict['SmallImage']


def get_book_medium_image(some_isbn):
    dict = get_book_info_as_dict(some_isbn)
    return dict['MediumImage']


def get_book_large_image(some_isbn):
    dict = get_book_info_as_dict(some_isbn)
    return dict['LargeImage']


if __name__ == "__main__":

    CC2_ISBN_10 = '0735619670'
    CC2_ISBN_13 = '9780735619678'

    print get_book_title(CC2_ISBN_10)
    print get_book_title(CC2_ISBN_13)
