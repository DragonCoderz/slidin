from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from slidin.models import User

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

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('An account is already associated with this email.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                         validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    remember =  BooleanField('Remember Me')
    submit = SubmitField('Login')