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
        db.posessions,
        fields = [db.posessions.item_name, db.posessions.notes, db.posessions.quality, db.posessions.return_date, db.posessions.picture],
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
    form = SQLFORM(db.posessions,
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
    query = (db.posessions.user_id == auth.user.id)
    grid = SQLFORM.grid(
        query,
        fields = [db.posessions.user_id, db.posessions.item_name, db.posessions.notes, db.posessions.quality, db.posessions.return_date, db.posessions.picture],
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
    query = (db.auth_user.id == db.friends.user_id)&(db.auth_user.id != auth.user.id)
    grid = SQLFORM.grid(
        query,
        fields = [db.auth_user.first_name, db.auth_user.last_name, db.auth_user.email],
        editable = False,
        create = False,
        user_signature = False,
        formname='web2py_grid',
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
