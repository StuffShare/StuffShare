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
	key_values = [(urllib2.quote(k), urllib2.quote(v)) for k,v in params.items()]
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

def get_book_info(isbn):
	params = {'ResponseGroup':'ItemAttributes,Images',
	          'AssociateTag':AWS_ASSOCIATE_ID,
	          'Operation':'ItemLookup',
	          'SearchIndex':'Books',
	          'IdType':'ISBN',
	          'ItemId':isbn}
	url = get_signed_url(params)

	response = http_get(url)
	xml_string = response.read()

	# remove the obnoxious namespace
	xml_string = re.sub(' xmlns="[^"]+"', '', xml_string, count = 1)

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
		if asin.text == isbn:
			# remove the 'ItemLinks' node
			itemLinks = item.find('ItemLinks')
			item.remove(itemLinks)
		else:
			items.remove(item)

	return xml_object

def get_book_title(isbn):
	root = get_book_info(isbn)
	element = root.find('Items/Item/ItemAttributes/Title')
	return element.text

def get_book_small_image(isbn):
	root = get_book_info(isbn)
	element = root.find('Items/Item/SmallImage/URL')
	return element.text

def get_book_medium_image(isbn):
	root = get_book_info(isbn)
	element = root.find('Items/Item/MediumImage/URL')
	return element.text

def get_book_large_image(isbn):
	root = get_book_info(isbn)
	element = root.find('Items/Item/LargeImage/URL')
	return element.text

# test