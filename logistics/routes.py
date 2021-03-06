# Imports
from logistics import app, db, bcrypt
from flask import Flask, redirect, render_template, url_for, flash
from logistics.forms import RegistrationForm, LoginForm
from logistics.models import User
from flask_login import login_user, current_user, logout_user

# Routes for different pages
@app.route('/')
def home():
    return 'Hello, World'


@app.route('/login', methods = ['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash("Login Unsuccessful. Please check email and password")
    return render_template('login.html', form = form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form =form)


@app.route("/logout")
def logout():
    logout_user()
    return "You have been logged out"


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')






if __name__ == '__main__':
    app.run(debug=True)