__author__ = 'IshanB'

# Adds (user_id, friend_id) and (friend_id, user_id)
@auth.requires_login()
def __new_friend(user_id, friend_id):
    db.friends.insert(user_id=user_id, friend_id=friend_id)
    db.friends.insert(friend_id=user_id, user_id=friend_id)
    return

def is_friend(user_id, friend_id):
    friend_query = (db.friends.user_id == user_id) & (db.friends.friend_id == friend_id)
    print "user_id:" + str(user_id) + "friend_id" + str(friend_id)

    if db(friend_query).count() == 0:
        return False
    return True