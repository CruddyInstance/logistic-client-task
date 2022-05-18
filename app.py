# Imports
from enum import unique
import bcrypt
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'c5272a1ed792b550511e4f43'
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # For creating the database and its location for flask
bcrypt = Bcrypt()


# The structure of table User in database.db
# This will also create the database we mentioned above
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False, unique = True)
    password = db.Column(db.String(80), nullable = False)




# Routes for different pages
@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')













if __name__ == '__main__':
    app.run(debug=True)