# dal/user_dal.py
from models.user_model import User
from app import db

def create_user(username, email, password):
    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

def find_user_by_email(email):
    return User.query.filter_by(email=email).first()
