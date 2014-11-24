__author__ = 'gwilliams'

import base64
import hmac
import urlparse
import time
import urllib2
import re

from hashlib import sha256 as sha256
from xml.etree import ElementTree as ET

AWS_ACCESS_KEY_ID = 'AKIAJSUR6X4TI3SSLYZA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_ASSOCIATE_ID = 'sc4p-20'

AWS_ACCESS_KEY_ID = 'AKIAJSUR6X4TI3SSLYZA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_ASSOCIATE_ID = 'sc4p-20'

# getSignedUrl from http://www.princesspolymath.com/princess_polymath/?p=182
def get_signed_url(params):
	action = 'GET'
	server = "webservices.amazon.com"
	path = "/onca/xml"

	params['Version'] = '2009-11-02'
	params['AWSAccessKeyId'] = AWS_ACCESS_KEY_ID
	params['Service'] = 'AWSECommerceService'
	params['Timestamp'] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

	# Now sort by keys and make the param string
	key_values = [(urllib2.quote(k), urllib2.quote(v)) for k,v in params.items()]
	key_values.sort()

	# Combine key value pairs into a string.
	paramstring = '&'.join(['%s=%s' % (k, v) for k, v in key_values])
	url = "http://" + server + path + "?" + ('&'.join(['%s=%s' % (k, v) for k, v in key_values]))

	# Add the method and path (always the same, how RESTy!) and get it ready to sign

	str = action + "\n" + server + "\n" + path + "\n" + paramstring
	my_hmac = hmac.new(AWS_SECRET_ACCESS_KEY, str, digestmod=sha256)

	# Sign it up and make the url string
	url = url + "&Signature=" + urllib2.quote(base64.encodestring(my_hmac.digest()).strip())

	return url

def get_book_info(isbn):
	params = {'ResponseGroup':'Small,ItemAttributes', #,Images
	          'AssociateTag':AWS_ASSOCIATE_ID,
	          'Operation':'ItemLookup',
	          'SearchIndex':'Books',
	          'IdType':'ISBN',
	          'ItemId':isbn}
	url = get_signed_url(params)
	response = urllib2.urlopen(url)
	xml_string = response.read()

	# remove the obnoxious namespace
	xml_string = re.sub(' xmlns="[^"]+"', '', xml_string, count = 1)

	# construct the xml object
	xml_object = ET.fromstring(xml_string)

	# remove the useless 'OperationRequest' node
	operationRequest = xml_object.find('OperationRequest')
	xml_object.remove(operationRequest)

	return xml_object

def get_book_title(isbn):
	root = get_book_info(isbn)
	title = root.find('Items/Item/ItemAttributes/Title')
	return title.text
