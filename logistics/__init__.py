from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'c5272a1ed792b550511e4f43'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # For creating the database and its location for flask
db = SQLAlchemy(app)



from logistics import routes