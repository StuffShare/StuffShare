__author__ = 'Michael Moo'


@auth.requires_login()
def lookup_isbn():
    return locals()


@auth.requires_login()
def lookup_movie():
    return locals()