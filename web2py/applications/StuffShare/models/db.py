# db = DAL('mysql://StuffShare:cmpt470@mysql.server/StuffShare$stuffshare') # Use when uploaded to PythonAnywhere
db = DAL('sqlite://storage.db')  # Use for offline testing


# AUTHENTICATION #
from gluon.tools import Auth

auth = Auth(db)
auth.define_tables(username=False, signature=False)

auth.settings.actions_disabled.append('request_reset_password')
auth.settings.actions_disabled.append('retrieve_username')


# POSSESSIONS #
db.define_table('possessions',
                Field('id', 'integer', unique=True, requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC()]),
                Field('user_id', 'integer'),
                Field('user_first_name', 'text'),
                Field('user_last_name', 'text'),
                Field('user_email', 'text'),
                Field('item_name', 'text'),
                Field('notes', 'text'),
                Field('location', 'text'),
                Field('quality', 'text'),
                Field('visibility', 'text'),
                Field('return_date', 'date'),
                Field('picture', 'upload'))

db.possessions.id.readable = False

db.possessions.user_id.requires = IS_NOT_EMPTY()
db.possessions.user_id.requires = IS_IN_DB(db, db.auth_user.id)

db.possessions.user_id.readable = False

db.possessions.user_first_name.requires = IS_NOT_EMPTY()
db.possessions.user_first_name.requires = IS_IN_DB(db, db.auth_user.first_name)

db.possessions.user_last_name.requires = IS_NOT_EMPTY()
db.possessions.user_last_name.requires = IS_IN_DB(db, db.auth_user.last_name)

db.possessions.user_email.requires = IS_NOT_EMPTY()
db.possessions.user_email.requires = IS_IN_DB(db, db.auth_user.email)
db.possessions.user_email.requires = IS_EMAIL()

db.possessions.item_name.requires = IS_NOT_EMPTY()

db.possessions.notes.requires = IS_NOT_EMPTY()

db.possessions.location.requires = IS_NOT_EMPTY()

db.possessions.quality.requires = IS_NOT_EMPTY()
db.possessions.quality.requires = IS_IN_SET(('Poor', 'Mediocre', 'Average', 'Good', 'Excellent', 'Like New'))

db.possessions.visibility.requires = IS_NOT_EMPTY()
db.possessions.visibility.requires = IS_IN_SET(('Public', 'Private'))

db.possessions.return_date.requires = IS_NOT_EMPTY()

db.possessions.picture.requires = IS_NOT_EMPTY()
db.possessions.picture.requires = requires = IS_IMAGE(extensions=('bmp', 'gif', 'jpeg', 'png'), maxsize=(4096, 4096),
                                                      minsize=(128, 128))


# FRIENDS #
db.define_table('friends',
                Field('id', 'integer', unique=True, requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC()]),
                Field('user_id', 'integer'),
                Field('friend_id', 'integer'))

db.friends.user_id.requires = IS_NOT_EMPTY()
db.friends.user_id.requires = IS_ALPHANUMERIC()
db.friends.user_id.requires = IS_IN_DB(db, db.auth_user.id)

db.friends.friend_id.requires = IS_NOT_EMPTY()
db.friends.friend_id.requires = IS_ALPHANUMERIC()
db.friends.friend_id.requires = IS_IN_DB(db, db.auth_user.id)

db.friends.id.readable = False


# FRIEND REQUESTS #
db.define_table('friend_requests',
                Field('id', 'integer', unique=True, requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC()]),
                Field('user_id', 'integer'),
                Field('friend_id', 'integer'))

db.friend_requests.user_id.requires = IS_NOT_EMPTY()
db.friend_requests.user_id.requires = IS_ALPHANUMERIC()
db.friend_requests.user_id.requires = IS_IN_DB(db, db.auth_user.id)

db.friend_requests.friend_id.requires = IS_NOT_EMPTY()
db.friend_requests.friend_id.requires = IS_ALPHANUMERIC()
db.friend_requests.friend_id.requires = IS_IN_DB(db, db.auth_user.id)

db.friend_requests.id.readable = False