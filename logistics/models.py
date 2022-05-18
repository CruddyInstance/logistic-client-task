from logistics import db 
from flask_login import UserMixin


# This will also create the database we mentioned above
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False, unique = True)
    email = db.Column(db.String(25), nullable = False)
    password = db.Column(db.String(80), nullable = False)
