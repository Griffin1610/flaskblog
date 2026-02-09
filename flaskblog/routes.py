from flaskblog import app, db, bcrypt
from flask import render_template, url_for, flash, redirect
from flaskblog.models import User, Post
from flaskblog.forms import RegistartionForm, LoginForm
from flask_login import login_user, logout_user
posts = [
    {
        'author' : 'Griffin Polly',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'February 5th, 2026',
    },
    {
        'author' : 'Griffin Polly',
        'title' : 'Blog Post 2',
        'content' : 'First post content',
        'date_posted' : 'February 5th, 2026'
    }
]

@app.route("/")  #route decorators, used to navigate between pages. define a function underneath that returns a html template
@app.route("/home") 
def home():
    return render_template("home.html", posts=posts) #render template returns html pages, any arguments we pass in give us access to variable in template

@app.route("/about")
def about():
    return render_template("about.html", title='About')

@app.route("/register", methods=["GET","POST"])
def register():
    form = RegistartionForm()
    if form.validate_on_submit():
        #hash password and create account
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"account created for {form.username.data}. You are now able to login", 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template("login.html", title="Login", form=form)

@app.route("/loguout")
def logout():
    logout_user()
    return redirect(url_for('home'))