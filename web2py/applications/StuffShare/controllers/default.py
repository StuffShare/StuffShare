def user():
    return dict(form=auth())


def index():
    if not session.flashed:
        response.flash=T('Welcome to StuffShare')
        session.flashed=True
    return dict(message=T('Welcome to StuffShare'))