__author__ = 'Gary Williams'

import re


def even(i):
    return i % 2 == 0


def format_isbn(some_isbn):
    return some_isbn.replace("-", "").replace(" ", "").upper()


def calc_isbn_10_check_digit(digits):
    checksum = sum(int(digit) * (i + 1) for i, digit in enumerate(digits))
    checkdigit_value = checksum % 11
    if checkdigit_value == 10:
        return 'X'
    else:
        return chr(checkdigit_value + ord('0'))


def calc_isbn_13_check_digit(digits):
    checksum = sum(int(digit) * (1 if (even(i)) else 3) for i, digit in enumerate(digits))
    checkdigit_value = 10 - checksum % 10
    return chr(checkdigit_value + ord('0'))


def is_valid_isbn_10(some_isbn):
    some_isbn = format_isbn(some_isbn)

    if len(some_isbn) != 10:
        return False

    match = re.search(r'^([0-9]{9})([0-9X])$', some_isbn)
    if not match:
        return False

    return match.group(2) == calc_isbn_10_check_digit(match.group(1))


def is_valid_isbn_13(some_isbn):
    some_isbn = format_isbn(some_isbn)

    if len(some_isbn) != 13:
        return False

    match = re.search(r'^([0-9]{12})([0-9])$', some_isbn)
    if not match:
        return False

    return match.group(2) == calc_isbn_13_check_digit(match.group(1))


def is_valid_isbn(some_isbn):
    return is_valid_isbn_10(some_isbn) or is_valid_isbn_13(some_isbn)

def convert_isbn_10_to_isbn_13(isbn10):
    isbn10 = format_isbn(isbn10)

    if not(is_valid_isbn_10(isbn10)):
        return isbn10 + ' is not a valid ISBN-10'

    isbn13_digits = '978' + isbn10[0:9]

    return isbn13_digits + calc_isbn_13_check_digit(isbn13_digits)

def convert_isbn_13_to_isbn_10(isbn13):
    isbn13 = format_isbn(isbn13)

    if not (is_valid_isbn_13(isbn13)):
        return isbn10 + ' is not a valid ISBN-13'

    isbn10_digits = isbn13[3:12]

    return isbn10_digits + calc_isbn_10_check_digit(isbn10_digits)

def fix_isbn(some_isbn):
    some_isbn = format_isbn(some_isbn)

    if is_valid_isbn_10(some_isbn):
        isbn10 = some_isbn
        isbn13 = convert_isbn_10_to_isbn_13(isbn10)
    else:
        if is_valid_isbn_13(some_isbn):
            isbn13 = some_isbn
            isbn10 = convert_isbn_13_to_isbn_10(isbn13)
        else:
            return some_isbn + ' is not a valid ISBN'

    return isbn10, isbn13

if __name__ == "__main__":
    CC2_ISBN_10 = '0735619670'
    CC2_ISBN_13 = '9780735619678'

    print is_valid_isbn_10(CC2_ISBN_10)
    print is_valid_isbn_13(CC2_ISBN_13)

    print CC2_ISBN_10 == convert_isbn_13_to_isbn_10(CC2_ISBN_13)
    print CC2_ISBN_13 == convert_isbn_10_to_isbn_13(CC2_ISBN_10)
