__author__ = 'Gary Williams'

import re




if __name__ == "__main__":
    CC2_ISBN_10 = '0735619670'
    CC2_ISBN_13 = '9780735619678'

    print is_valid_isbn_10(CC2_ISBN_10)
    print is_valid_isbn_13(CC2_ISBN_13)

    print CC2_ISBN_10 == convert_isbn_13_to_isbn_10(CC2_ISBN_13)
    print CC2_ISBN_13 == convert_isbn_10_to_isbn_13(CC2_ISBN_10)
