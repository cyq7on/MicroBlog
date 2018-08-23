from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from app.models import User
from flask_login import current_user, login_user, logout_user


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'cyq7on 燕'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'post'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if user is None or user.check_pwd(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
