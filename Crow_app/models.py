from Crow_app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
import os


############# UTILITILIS #############

def new_gallery(name):
    name = f"\{name}"
    location =os.path.abspath(os.path.dirname(__file__))+r"\static\uploads\products"+name
    os.mkdir(location)
    return location


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def load_users():
    if current_user.is_authenticated():
        return current_user
    else:
        return None




############### MODELS ###############

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique =True, index=True)
    username = db.Column(db.String(64), unique =True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self,email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
    

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)

    def reset_password(password):
        return generate_password_hash(password)

class Task(db.Model):
    __tablename__ = 'tasks'
    
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer)
    task = db.Column(db.String)
    status = db.Column(db.String)

    def __init__(self,user_id, task, status):
        self.user = user_id
        self.task = task
        self.status = status


class Product(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    owner = db.Column(db.String)
    name = db.Column(db.String)
    description =db.Column(db.String)
    part_id = db.Column(db.Integer)
    gallery = db.Column(db.String)
    main_photo = db.Column(db.String)
    status = db.Column(db.String)

    def __init__(self,user_id, owner, name, description,part_id,main_photo,status):
        self.gallery= new_gallery(name)
        self.owner= owner
        self.user_id = user_id
        self.name = name
        self.description = description
        self.part_id = part_id
        main_photo = main_photo
        self.status = status
