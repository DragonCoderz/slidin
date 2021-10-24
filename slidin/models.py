from slidin import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model):
    #perhaps set username as primary key?
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),  unique=True, nullable=False)

#     #one to many relationship, one user to many images
#     posts = db.relationship('UserImagePost', backref='author', lazy=True)

# class UserImagePost(db.Model):
#     id = db.Column(db.Integer, primary_key=True)

#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     #one to many relationship, one image to many users in image?
#     users = db.relationship('User', backref='image', lazy=True)
    
#     #email = db.Column(db.String(120), unique=True, nullable=False) 
#     image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     #password = db.Column(db.String(60), nullable=False)   

#     def __repr__(self):
#         return f"UserImagePost('{self.user_id}', '{self.date_posted}', '{self.image_file}')"