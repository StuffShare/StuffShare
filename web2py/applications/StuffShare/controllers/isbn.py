__author__ = 'gwilliams'

import re

def format_isbn(isbn):
	return isbn.replace("-", "").replace(" ", "").upper()

def calc_isbn_10_check_digit(digits):
	checksum = sum(int(digit) * (i + 1) for i, digit in enumerate(digits))
	checkdigit_value = checksum % 11
	if (checkdigit_value == 10):
		return 'X'
	else:
		return chr(checkdigit_value + ord('0'))

def even(i):
	return i % 2 == 0

def calc_isbn_13_check_digit(digits):
	checksum = sum(int(digit) * (1 if (even(i)) else 3) for i, digit in enumerate(digits))
	checkdigit_value = 10 - checksum % 10
	return chr(checkdigit_value + ord('0'))
	
def is_valid_isbn_10(isbn):
	isbn = format_isbn(isbn)

	if len(isbn) != 10:
		return False

	match = re.search(r'^([0-9]{9})([0-9]|X)$', isbn)
	if not match:
		return False

	return match.group(2) == calc_isbn_10_check_digit(match.group(1))

def is_valid_isbn_13(isbn):
	isbn = format_isbn(isbn)

	if len(isbn) != 13:
		return False
		
	match = re.search(r'^([0-9]{12})([0-9])$', isbn)
	if not match:
		return False

	return match.group(2) == calc_isbn_13_check_digit(match.group(1))

def is_valid_isbn(isbn):
	return is_valid_isbn_10(isbn) or is_valid_isbn_13(isbn)
	
def convert_isbn_13_to_isbn_10(isbn13):
	isbn13 = format_isbn(isbn13)

	if not(is_valid_isbn_13(isbn13)):
		return 'INVALID'

	isbn10_digits = isbn13[3:12]

	return isbn10_digits + calc_isbn_13_check_digit(isbn10_digits)

if __name__ == "__main__":

	print is_valid_isbn_10('020170353X')
	print is_valid_isbn_13('978-0-306-406157')
	print convert_isbn_13_to_isbn_10('978-0-306-406157')
