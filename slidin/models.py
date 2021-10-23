from slidin import db
from datetime import datetime

class User(db.Model):
    #perhaps set username as primary key?
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),  unique=True, nullable=False)
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