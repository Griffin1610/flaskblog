from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
load_dotenv()

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.config['SECRET_KEY']= os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
from flaskblog import routes