__author__ = 'IshanB'

# Adds (user_id, friend_id) and (friend_id, user_id)
@auth.requires_login()
def __new_friend(user_id, friend_id):
    db.friends.insert(user_id=user_id, friend_id=friend_id)
    db.friends.insert(friend_id=user_id, user_id=friend_id)
    return
