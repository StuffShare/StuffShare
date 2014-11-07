def user():
    return dict(form=auth())

def index():
    if not session.flashed:
        response.flash=T('Welcome to StuffShare')
        session.flashed=True
    return dict(message=T('Welcome to StuffShare'))

@auth.requires_login()
def item_manager():
    grid = SQLFORM.grid(
        db.posessions,
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
