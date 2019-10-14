import os

class BaseConfig(object):
    
    ## Database Config
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://%s:%s@%s/%s' % (
        # ARGS.dbuser, ARGS.dbpass, ARGS.dbhost, ARGS.dbname
        os.environ['DBUSER'], os.environ['DBPASS'], os.environ['DBHOST'], os.environ['DBNAME']
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LoginConfig(object):
    
    WTF_CSRF_SECRET_KEY = "b'f\xfa\x8b{X\x8b\x9eM\x83l\x19\xad\x84\x08\xaa"