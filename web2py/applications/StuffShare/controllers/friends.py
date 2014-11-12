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