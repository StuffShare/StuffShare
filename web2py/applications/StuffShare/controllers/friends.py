@auth.requires_login()
def friend_list():
    query = (db.auth_user.id == db.friends.friend_id) & (auth.user.id == db.friends.user_id)
    query &= (db.friends.friend_id != auth.user_id)
    friends = db(query).select(db.auth_user.ALL)
    return dict(friends=friends)


@auth.requires_login()
def user_list():
    users = db().select(db.auth_user.first_name, db.auth_user.last_name, db.auth_user.id)
    return dict(users=users)


@auth.requires_login()
def request_friend():
    db.friend_requests.insert(user_id=auth.user.id, friend_id=request.vars.friend_id)
    redirect(URL('user_list'))
    return


@auth.requires_login()
def delete_friend():
    friend_id = request.vars.friend_id

    query = ((db.friends.user_id == auth.user.id) & (db.friends.friend_id == friend_id)) | \
            ((db.friends.friend_id == auth.user.id) & (db.friends.user_id == friend_id))

    db(query).delete()

    redirect(URL('friend_list'))
    return

@auth.requires_login()
def get_friend_code():
    query = (db.auth_user.id == auth.user_id)
    friend_code = db(query).select(db.auth_user.id)
    return dict(friend_code=friend_code)


# Returns the id, first name, last name and email of the friend that requested to be added
@auth.requires_login()
def friend_requests():
    query = (db.auth_user.id == db.friend_requests.user_id) & (auth.user.id == db.friend_requests.friend_id)
    query &= (db.friend_requests.user_id != auth.user_id)
    friend_request_list = db(query).select(db.auth_user.id, db.auth_user.first_name, db.auth_user.last_name,
                                           db.auth_user.email)
    return dict(friend_request_list=friend_request_list)


@auth.requires_login()
def accept_friend_request():
    friend_id = request.vars.friend_id

    #Current user is the friend that is added, friend is the user that the current user is declining
    query = db.friend_requests.friend_id == auth.user.id
    query &= db.friend_requests.user_id == friend_id

    __new_friend(auth.user.id, friend_id)

    db(query).delete()

    redirect(URL('friend_requests'))
    return


# Deletes entry on friend_request table with friend_id == current user and user_id == friend that requested to be added
@auth.requires_login()
def decline_friend_request():
    friend_id = request.vars.friend_id

    #Current user is the friend that is added, friend is the user that the current user is declining
    query = db.friend_requests.friend_id == auth.user.id
    query &= db.friend_requests.user_id == friend_id

    db(query).delete()

    redirect(URL('friend_requests'))
    return