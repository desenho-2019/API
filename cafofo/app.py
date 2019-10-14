import os
from flask import Flask, render_template, request, redirect, url_for,flash
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import *
from flask_login import LoginManager, login_user, current_user, logout_user


app = Flask(__name__)
app.config.from_object(BaseConfig)
api = Api(app)

#Inicializing database connection
db = SQLAlchemy(app)

def main():
    db.create_all()

#inicializing database migration 
migrate = Migrate(app,db)


app.secret_key='super secret'
app.config.from_object(LoginConfig)
# Initialize login manager
login = LoginManager(app)
login.init_app(app)


from wtform_fields import *
from models import *


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route("/", methods=['GET', 'POST'])
def index():

    reg_form = RegistrationForm()

    # Update database if validation success
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        # Hash password
        hashed_pswd = pbkdf2_sha256.hash(password)

        # Add username & hashed password to DB
        user = User(username=username, hashed_pswd=hashed_pswd)
        db.session.add(user)
        db.session.commit()

        flash('Registered successfully. Please login.', 'success')
        return redirect(url_for('login'))

    return render_template("index.html", form=reg_form)


@app.route("/login", methods=['GET', 'POST'])
def login():

    login_form = LoginForm()

    # Allow login if validation success
    if login_form.validate_on_submit():
    #    user_object = User.query.filter_by(username=login_form.username.data).first()
    #    login_user(user_object)
        return redirect(url_for('teste'))

    return render_template("login.html", form=login_form)


@app.route("/logout", methods=['GET'])
def logout():

    # Logout user
    logout_user()
    flash('You have logged out successfully', 'success')
    return redirect(url_for('login'))

@app.route("/teste", methods=['GET','POST'])
def teste():

    return render_template("teste.html")
#class HelloWorld(Resource):
#    def get(self):
#        return {'Hello': 'world'}
#api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

