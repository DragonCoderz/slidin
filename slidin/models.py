from slidin import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model):
    #perhaps set username as primary key?
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),  unique=True, nullable=False)

    #one to many relationship, one user to many images
    posts = db.relationship('UserImagePost', backref='author', lazy=True)

    #how our objects are printed out  
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"