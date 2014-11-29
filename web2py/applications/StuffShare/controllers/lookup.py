__author__ = 'Gary Williams, Michael Moo, Ishan Bhutani'


@auth.requires_login()
def lookup_isbn():
    form = FORM('ISBN:', INPUT(_name='isbn'), INPUT(_type='submit',
                                                    _value='Submit'))
    if form.process().accepted:
        redirect(URL(f='get_book_info_as_dict', c='amazon', vars={'some_isbn':form.vars.isbn}))
        return

    return dict(form=form)


@auth.requires_login()
def lookup_movie():
    return locals()