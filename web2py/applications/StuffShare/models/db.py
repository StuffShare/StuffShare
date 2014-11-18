#db = DAL('mysql://clan10:clan10@mysql.server/clan10$stuffshare') #this connects to the mysql server running on python anywhere; will not work unless the app is running on pythonanywhere
#This uses a local data-based sql server, PLEASE UPLOAD TO PYTHONANYWHERE and TEST ON SERVER BEFORE COMMITTING!
# ALSO PLEASE COMMENT THIS AND UNCOMMENT THE PROPER MYSQL STRING
db = DAL('sqlite://storage.db')

from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=False, signature=False)

auth.settings.actions_disabled.append('request_reset_password')
auth.settings.actions_disabled.append('retrieve_username')


db.define_table('possessions',
    Field('id', 'integer', unique=True, requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC()]),
    Field('user_id', 'integer'),
    Field('item_name', 'text'),
    Field('notes', 'text'),
    Field('location', 'text'),
    Field('quality', 'text'),
    Field('visibility', 'text'),
    Field('return_date', 'date'),
    Field('picture', 'upload'))

db.possessions.user_id.requires = IS_NOT_EMPTY()
db.possessions.user_id.requires = IS_IN_DB(db, db.auth_user.id)
db.possessions.item_name.requires = IS_NOT_EMPTY()
db.possessions.notes.requires = IS_NOT_EMPTY()
db.possessions.location.requires = IS_NOT_EMPTY()
db.possessions.quality.requires = IS_NOT_EMPTY()
db.possessions.visibility.requires = IS_NOT_EMPTY()
db.possessions.return_date.requires = IS_NOT_EMPTY()

db.possessions.visibility.requires=IS_IN_SET(('Public', 'Private'))
db.possessions.quality.requires=IS_IN_SET(('Poor','Mediocre','Average', 'Good', 'Excellent', 'Like New'))
db.possessions.picture.requires=requires=IS_IMAGE(extensions=('bmp', 'gif', 'jpeg', 'png'), maxsize=(10000, 10000), minsize=(0, 0))

db.possessions.id.readable = False
db.possessions.user_id.readable = False


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