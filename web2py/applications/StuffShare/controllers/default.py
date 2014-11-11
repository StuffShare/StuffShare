def user():
    return dict(form=auth())


def index():
    if not session.flashed:
        response.flash=T('Welcome to StuffShare')
        session.flashed=True
    return dict(message=T('Welcome to StuffShare'))


@auth.requires_login()
def item_list():
    grid = SQLFORM.grid(
        db.possessions,
        fields = [db.possessions.item_name, db.possessions.notes, db.possessions.quality, db.possessions.return_date, db.possessions.picture],
        user_signature = False,
        deletable = False,
        editable = False,
        create = False,
        formname = 'web2py_grid',
        exportclasses = dict(
            csv_with_hidden_cols = False,
            xml = False,
            html = False,
            csv = False,
            json = False,
            tsv_with_hidden_cols = False,
            tsv = False
        )
    )
    return dict(grid=grid)


@auth.requires_login()
def add_item():
    form = SQLFORM(db.possessions,
        fields = ['item_name', 'notes', 'quality', 'return_date', 'picture'],
    )
    form.vars.user_id = auth.user.id
    if form.process().accepted:
       response.flash = 'Item Added.'
    elif form.errors:
       response.flash = 'Item was not Added!'
    return dict(form=form)


@auth.requires_login()
def user_item_list():
    query = (db.possessions.user_id == auth.user.id)
    grid = SQLFORM.grid(
        query,
        fields = [db.possessions.user_id, db.possessions.item_name, db.possessions.notes, db.possessions.quality, db.possessions.return_date, db.possessions.picture],
        user_signature = False,
        create = False,
        formname = 'web2py_grid',
        exportclasses = dict(
            csv_with_hidden_cols = False,
            xml = False,
            html = False,
            csv = False,
            json = False,
            tsv_with_hidden_cols = False,
            tsv = False
        )
    )
    return dict(grid=grid)


@auth.requires_login()
def friend_list():
    query = (db.auth_user.id == db.friends.friend_id)&(auth.user.id == db.friends.user_id)&(db.friends.friend_id != auth.user_id)
    friends = db(query).select(db.auth_user.ALL)
    return dict(friends=friends)


@auth.requires_login()
def add_friend():
    form = SQLFORM(db.friends,
        fields = ['friend_id'],
    )
    form.vars.user_id = auth.user.id
    if form.process().accepted:
       response.flash = 'Item Added.'
    elif form.errors:
       response.flash = 'Item was not Added!'
    return dict(form=form)


@auth.requires_login()
def friend_requests():
    query = (db.auth_user.id == db.friends.friend_id)&(auth.user.id == db.friends.user_id)&(db.friends.friend_id != auth.user_id)
    friends = db(query).select(db.auth_user.ALL)
    return dict(friends=friends)
