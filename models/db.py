
from gluon.contrib.appconfig import AppConfig
from gluon.tools import Auth
configuration = AppConfig(reload=True)

db= DAL("sqlite://storage.sqlite")
auth = Auth(db)
auth.define_tables(username=True)

db.define_table('document',
                Field('title', unique=True),
                Field('file', 'upload'),
                format='%(title)s')

db.document.title.require = IS_NOT_IN_DB(db,db.document.title)
