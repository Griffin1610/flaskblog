from flask import Flask, render_template, url_for, flash, redirect
from flask_bootstrap import Bootstrap5
from forms import RegistartionForm, LoginForm
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.config['SECRET_KEY']= os.getenv('SECRET_KEY')

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
        flash(f"account created for {form.username.data}", 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template("login.html", title="Login", form=form)

if __name__ == '__main__':
    app.run(debug=True)