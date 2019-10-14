import os
from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import BaseConfig


app = Flask(__name__)
app.config.from_object(BaseConfig)
api = Api(app)

#Inicializing database connection
db = SQLAlchemy(app)

#inicializing database migration 
migrate = Migrate(app,db)



from models import *

class HelloWorld(Resource):
    def get(self):
        return {'Hello': 'world'}
api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True,host='0.0.0.0')