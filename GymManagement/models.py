from . import db
# , login_manager
from . import bcrypt
# from flask_login import UserMixin

class Member(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=40), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    phonenumber = db.Column(db.Integer(), nullable=False)
    gender = db.Column(db.String(length=10), nullable=False)
    dob = db.Column(db.Integer(), nullable = False)
    regdate = db.Column(db.Integer(), nullable = False)
    membership_available= db.Column(db.Integer(), nullable = False)
    address = db.Column(db.String(length=30), nullable=False)
    img = db.Column(db.String(150), default = 'image.jpg')
    def __repr__(self):
        return "<item %r>" %self.name

class Trainer(db.Model):
    id = db.Column(db.Integer(), primary_key=True)   
    name = db.Column(db.String(length=40), nullable=False, unique=True)     
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    phonenumber = db.Column(db.Integer(), nullable=False)
    gender = db.Column(db.String(length=10), nullable=False)
    dob = db.Column(db.Integer(), nullable = False)
    regdate = db.Column(db.Integer(), nullable = False)
    address = db.Column(db.String(length=30), nullable=False)
    img = db.Column(db.String(150), default = 'image.jpg')
    def __repr__(self):
        return "<item %r>" %self.name