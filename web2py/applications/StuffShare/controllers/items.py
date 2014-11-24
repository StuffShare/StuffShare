__author__ = 'MichaelM'

@auth.requires_login()
def public_item_list():
    query = (db.possessions.visibility == 'Public')

    grid = SQLFORM.grid(
        query,
        fields=[db.possessions.item_name, db.possessions.user_first_name, db.possessions.user_last_name,
                db.possessions.user_email, db.possessions.quality, db.possessions.location, db.possessions.return_date,
                db.possessions.picture],
        user_signature=False,
        deletable=False,
        editable=False,
        create=False,
        formname='web2py_grid',
    )

    return dict(grid=grid)


@auth.requires_login()
def private_item_list():
    friend_query = (db.friends.user_id == auth.user_id)
    friend_list = db(friend_query).select(db.friends.friend_id)

    private_items_query = (db.possessions.visibility == 'Private')

    #Only show rows which have a friend id that corresponds to current user's friends
    friend_exists_query = False
    for friend in friend_list:
        friend_exists_query |= db.possessions.user_id == friend.friend_id

    private_items_query &= friend_exists_query

    grid = SQLFORM.grid(
        private_items_query,
        fields=[db.possessions.item_name, db.possessions.user_first_name, db.possessions.user_last_name,
                db.possessions.user_email, db.possessions.quality, db.possessions.location, db.possessions.return_date,
                db.possessions.picture],
        user_signature=False,
        deletable=False,
        editable=False,
        create=False,
        formname='web2py_grid',
    )

    return dict(grid=grid)


@auth.requires_login()
def user_item_list():
    query = (db.possessions.user_id == auth.user.id)

    db.possessions.user_id.readable = False
    db.possessions.user_id.writable = False
    db.possessions.user_first_name.writable = False
    db.possessions.user_last_name.writable = False
    db.possessions.user_email.writable = False

    grid = SQLFORM.grid(
        query,
        fields=[db.possessions.item_name, db.possessions.user_first_name, db.possessions.user_last_name,
                db.possessions.user_email, db.possessions.quality, db.possessions.location, db.possessions.return_date,
                db.possessions.picture],
        user_signature=False,
        create=False,
        formname='web2py_grid',
    )

    db.possessions.user_id.readable = False
    db.possessions.user_first_name.writable = True
    db.possessions.user_last_name.writable = True
    db.possessions.user_email.writable = True

    return dict(grid=grid)


@auth.requires_login()
def add_item():
    form = SQLFORM(db.possessions,
                   fields=['item_name', 'notes', 'quality', 'location', 'visibility', 'return_date', 'picture']
    )

    form.vars.user_id = auth.user.id
    form.vars.user_first_name = auth.user.first_name
    form.vars.user_last_name = auth.user.last_name
    form.vars.user_email = auth.user.email

    if form.process().accepted:
        response.flash = 'Item Added.'
    elif form.errors:
        response.flash = 'Item was not Added!'

    return dict(form=form)