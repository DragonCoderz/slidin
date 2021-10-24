from flask import  render_template, url_for, flash, redirect, request
from wtforms.validators import Email
from slidin import app, db, bycrypt
from slidin.models import User, UserImagePost
from slidin.forms import RegistrationForm, LoginForm
from werkzeug.utils import secure_filename
import boto3
from interface import bucket

@app.route("/")
@app.route("/userProfile")
def userProfile():
    return render_template('userProfile.html')
    
@app.route("/search")
def search():
    return render_template('search.html')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        s3 = boto3.client('s3')
        hashed_password = bycrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password,firstName=form.firstName.data, lastName=form.lastName.data)
        img = request.files['file']
        if img:
            filename = secure_filename(img.filename)
            img.save(filename)
            s3.upload_file(
                Bucket = bucket,
                Filename=filename,
                Key = filename
            )
            msg = "Upload Done ! "
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to login', 'success')
        return redirect(url_for('login'))
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