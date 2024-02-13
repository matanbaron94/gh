import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret_key"
basedir =  os.path.abspath(os.path.dirname(__file__))


###########  DATABASE  ############
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


############## LOGIN CONFIG #################
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


############### BLUEPRINTS ##################
from Crow_app.users.views import users
from Crow_app.tasks.views import tasksr
from Crow_app.products.views import productsr
from Crow_app.real_time.views import real_time

app.register_blueprint(users)
app.register_blueprint(tasksr)
app.register_blueprint(productsr)
app.register_blueprint(real_time)


################# UTILITIS ###############
def new_gallery(name):
    name = f"\{name}"
    location =os.path.abspath(os.path.dirname(__file__))+r"\static\uploads\products"+name
    os.mkdir(location)
    return location