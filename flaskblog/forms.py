from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flaskblog.models import User

class RegistartionForm(FlaskForm):
    username=StringField("username", validators=[DataRequired(), Length(min=2, max = 20)])
    email=StringField("email", validators=[DataRequired(), Email()])

    password=PasswordField("password", validators=[DataRequired()])
    confirm_password=PasswordField("confirm password", validators=[DataRequired(), EqualTo("password")])

    submit = SubmitField('sign up')

    #stop duplicate users (already has account)
    def vaildate_field(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken, please choose a different one')
        
    def vaildate_email(self, email):
        user = User.query.filter_by(username=email.data).first()
        if user:
            raise ValidationError('That email already exists in system, please choose a different one')

class LoginForm(FlaskForm):
    email=StringField("email", validators=[DataRequired(), Email()])

    password=PasswordField("password", validators=[DataRequired()])
    remember = BooleanField('remember me')

    submit = SubmitField('Login')