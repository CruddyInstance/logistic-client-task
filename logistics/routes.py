# Imports
from logistics import app, db
from enum import unique
from flask import Flask, redirect, render_template, url_for, flash
from logistics.forms import RegistrationForm, LoginForm
from logistics.models import User
from flask_bcrypt import Bcrypt



bcrypt = Bcrypt(app)

# Routes for different pages
@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/login', methods = ['POST', 'GET'])
def login():
    form = LoginForm()
    return render_template('login.html', form = form)


@app.route('/register', methods = ['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form =form)













if __name__ == '__main__':
    app.run(debug=True)