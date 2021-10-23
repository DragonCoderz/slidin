from enum import unique
from logging import debug
from os import truncate
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref 
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ef89e27fedbcc1b6bc2deeeac4b97600'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) 

class User(db.Model):
    #perhaps set username as primary key?
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    
    #one to many relationship, one user to many images
    posts = db.relationship('UserImagePost', backref='author', lazy=True)

    #how our objects are printed out  
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class UserImagePost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    #one to many relationship, one image to many users in image?
    users = db.relationship('User', backref='image', lazy=True)

    #email = db.Column(db.String(120), unique=True, nullable=False) 
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #password = db.Column(db.String(60), nullable=False)   



    def __repr__(self):
        return f"UserImagePost('{self.user_id}', '{self.date_posted}', '{self.image_file}')"
posts = [
    {
        'date': 'this is a date',
        'title': 'Title: Blog Post 1',
        'user': 'I am this person',
        'content': 'content stuff'
    }
]

@app.route("/")
@app.route("/userProfile")
def userProfile():
    return render_template('userProfile.html', posts=posts)
    
@app.route("/search")
def search():
    return render_template('search.html')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('userProfile'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@slidin.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('userProfile'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
