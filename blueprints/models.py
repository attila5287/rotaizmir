from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from blueprints import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(32), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    
    # Collect user posts, adm_notes and requests
    posts = db.relationship('Post', backref='author', lazy=True)
    notes = db.relationship('Note', backref='by_admin', lazy=True)
    requests = db.relationship('Request', backref='by_user', lazy=True)
    
    # Generate random int
    img_url = db.Column(db.Integer, nullable=False, default =0)
    is_admin = db.Column(db.String(32), nullable=False, default='n')
    is_member = db.Column(db.String(32), nullable=False, default='n')
    is_prez = db.Column(db.String(32), nullable=False, default='n')
    
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Nickname(db.Model):
    pass
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(256), nullable=False)

class Color(db.Model):
    pass
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(16), nullable=False)
    colorcode = db.Column(db.String(8), nullable=False)
    
class Member(db.Model): 
    pass
    id =  db.Column(db.Integer, nullable=False, primary_key=True)
    first_name =  db.Column(db.String(256), nullable=False)
    middle_name =  db.Column(db.String(256), nullable=True)
    last_name =  db.Column(db.String(256), nullable=False)
    phone_num =  db.Column(db.String(256), nullable=True)
    email =  db.Column(db.String(256), nullable=True)
    gender  =  db.Column(db.String(8), nullable=False)
    is_prez  =  db.Column(db.String(8), nullable=False)
    is_admin  =  db.Column(db.String(8), nullable=False)
    user_id =  db.Column(db.Integer, nullable=True)
    img_url =  db.Column(db.String(256), nullable=True)
    linkedin =  db.Column(db.String(256), nullable=True)
    twitter =  db.Column(db.String(256), nullable=True)
    instagram =  db.Column(db.String(256), nullable=True)

class Request(db.Model):
    pass
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    admin_id = db.Column(db.Integer, nullable=False)    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)    
