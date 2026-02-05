from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5
app = Flask(__name__)
bootstrap = Bootstrap5(app)

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


if __name__ == '__main__':
    app.run(debug=True)