__author__ = 'Ishan Bhutani'

@auth.requires_login()
def user_list():
    query = db.auth_user.id != auth.user.id
    #users = db(query).select(db.auth_user.first_name, db.auth_user.last_name, db.auth_user.id)

    # db.auth_user.id.readable = False
    grid = SQLFORM.grid(
        query,
        fields=[db.auth_user.first_name, db.auth_user.last_name],
        user_signature=False,
        create=False,
        editable=False,
        deletable=False,
        formname='web2py_grid'
    )

    if request.args(0) == "view":
        friend_query = (db.auth_user.id == request.args(2))
        users = db(friend_query).select(db.auth_user.ALL)
        response.view = "users/user_profile.html"
        return dict(user=users[0])

    # return dict(users=users)
    return dict(grid=grid)