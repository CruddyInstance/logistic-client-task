# Imports
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SECRET_KEY'] = 'c5272a1ed792b550511e4f43'


# Routs for different pages
@app.route('/')
def hello_world():
    return 'Hello, World!'















if __name__ == '__main__':
    app.run(debug=True)