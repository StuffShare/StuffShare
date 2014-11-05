db = DAL('mysql://clan10:clan10@mysql.server/clan10$authentication')
from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=False,signature=False)

db.define_table('posessions',
    Field('id', unique=True, requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC()]),
    Field('item_name', requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC()]),
    Field('quality', requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC()]))
