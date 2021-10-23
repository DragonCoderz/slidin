from flask import  render_template, url_for, flash, redirect
from slidin import app
from slidin.models import User, UserImagePost
from slidin.forms import RegistrationForm, LoginForm

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
