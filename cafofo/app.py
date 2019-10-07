import os
from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

## Database Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://%s:%s@%s/%s' % (
    # ARGS.dbuser, ARGS.dbpass, ARGS.dbhost, ARGS.dbname
    os.environ['DBUSER'], os.environ['DBPASS'], os.environ['DBHOST'], os.environ['DBNAME']
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class HelloWorld(Resource):
    def get(self):
        return {'Hello': 'world'}
api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')