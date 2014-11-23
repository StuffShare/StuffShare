__author__ = 'gwilliams'

import base64
import hmac
import urlparse
import time
import urllib2

from hashlib import sha256 as sha256

AWS_ACCESS_KEY_ID = 'AKIAJSUR6X4TI3SSLYZA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_ASSOCIATE_ID = 'sc4p-20' # Amazon generated this from the string "SFU CMPT 470 Project"

hmac = hmac.new(AWS_SECRET_ACCESS_KEY, digestmod=sha256)

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
	urlstring = "http://" + server + path + "?" + ('&'.join(['%s=%s' % (k, v) for k, v in key_values]))

	# Add the method and path (always the same, how RESTy!) and get it ready to sign
	hmac.update(action + "\n" + server + "\n" + path + "\n" + paramstring)

	# Sign it up and make the url string
	urlstring = urlstring + "&Signature=" + urllib2.quote(base64.encodestring(hmac.digest()).strip())

	return urlstring

def get_book_info(isbn):
	params = {'ResponseGroup':'Small,Images,AlternateVersions',
	          'AssociateTag':AWS_ASSOCIATE_ID,
	          'Operation':'ItemLookup',
	          'SearchIndex':'Books',
	          'IdType':'ISBN',
	          'ItemId':isbn}
	url = get_signed_url(params)
	response = urllib2.urlopen(url)
	return response.read()
