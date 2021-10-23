from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                         validators=[DataRequired(), Email()])
    firstName = StringField('First Name', 
                            validators=[DataRequired(), Length(min=1)])
    lastName = StringField('Last Name', 
                            validators=[DataRequired(), Length(min=1)])
                            
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_Password = PasswordField('Confirm Password', 
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                         validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    remember =  BooleanField('Remember Me')
    submit = SubmitField('Login')