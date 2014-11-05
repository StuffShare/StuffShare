def user():
    return dict(form=auth())

def index():
    return "Hello!"

@auth.requires_login()
def item_manager():
    grid = SQLFORM.grid(
        db.posessions,
        user_signature = False,
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
