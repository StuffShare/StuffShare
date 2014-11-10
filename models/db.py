db = DAL('mysql://clan10:clan10@mysql.server/clan10$stuffshare')
from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=False,signature=False)

auth.settings.actions_disabled.append('request_reset_password')
auth.settings.actions_disabled.append('retrieve_username')


db.define_table('posessions',
    Field('id', 'integer', unique=True, requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC()]),
    Field('user_id', 'integer', requires=[IS_NOT_EMPTY(), IS_IN_DB(db, db.auth_user.id)]),
    Field('item_name', 'text', requires=[IS_NOT_EMPTY()]),
    Field('notes', 'text', requires=[IS_NOT_EMPTY()]),
    Field('quality', 'text', requires=[IS_NOT_EMPTY()]),
    Field('return_date', 'date', requires=[IS_NOT_EMPTY()]),
    Field('picture', 'upload'))

db.posessions.quality.requires=IS_IN_SET(('Poor','Mediocre','Average', 'Good', 'Excellent', 'Like New'))
db.posessions.id.readable = False
db.posessions.user_id.readable = False


db.define_table('friends',
    Field('id', 'integer', unique=True, requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC()]),
    Field('user_id', 'integer', db.auth_user, requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC(), IS_IN_DB(db, db.auth_user.id)]),
    Field('friend_id', 'integer', db.auth_user, requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC(), IS_IN_DB(db, db.auth_user.id)]))

db.friends.id.readable = False
