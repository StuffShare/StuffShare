@auth.requires_login()
def public_item_list():
    query = (db.possessions.visibility == 'Public')
    grid = SQLFORM.grid(
        query,
        fields = [db.possessions.user_first_name, db.possessions.user_last_name, db.possessions.user_email, db.possessions.item_name, db.possessions.notes, db.possessions.location, db.possessions.quality, db.possessions.location, db.possessions.return_date, db.possessions.picture],
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
def private_item_list():
    query = (db.possessions.visibility == 'Private')
    grid = SQLFORM.grid(
        query,
        fields = [db.possessions.user_first_name, db.possessions.user_last_name, db.possessions.user_email, db.possessions.item_name, db.possessions.notes, db.possessions.location, db.possessions.quality, db.possessions.location, db.possessions.return_date, db.possessions.picture],
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
def user_item_list():
    query = (db.possessions.user_id == auth.user.id)
    grid = SQLFORM.grid(
        query,
        fields = [db.possessions.user_first_name, db.possessions.user_last_name, db.possessions.user_email, db.possessions.item_name, db.possessions.notes, db.possessions.location, db.possessions.quality, db.possessions.location, db.possessions.return_date, db.possessions.picture],
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
def add_item():
    form = SQLFORM(db.possessions,
        fields = ['item_name', 'notes', 'quality', 'location', 'visibility', 'return_date', 'picture'],
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
