from Crow_app import db
from flask import render_template, redirect, request, url_for, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from Crow_app.models import User, Task, Product
from Crow_app.users.forms import LoginForm, RegistrationForm

from werkzeug.security import generate_password_hash,check_password_hash
import os
from bme280pi import Sensor
from flask import jsonify
import json
# vluprint setup
real_time = Blueprint('real_time', __name__)


################# ROUTES ##################

@real_time.route('/real_time')
def real_time_page():
    return render_template('real_time.html')

@real_time.route('/real_time/get_status')
def get_status():
    try:
        sensor2 = Sensor(address=0x77)
        data = sensor2.get_data()
    except:
        data = {'temperature': "@@", 'pressure': "@@", 'humidity': "@@"}
    
    return jsonify(data)
   






# @users.route('/user/<username>',methods=['POST','GET'])
# def user(username):
#     form = NewTask()
#     user = current_user
#     products = Product.query.filter_by(user_id=user.id)
#     tasks = Task.query.filter_by(user=user.id)
#     return render_template("user.html", user =user, products= products, tasks = tasks, form= form)

# @users.route('/welcome')
# @login_required
# def welcome_user():
#     return render_template('welcome_user.html')


# @users.route('/reset-password/<username>', methods=['GET','POST'])
# def reset_password(username):
#     form = RegistrationForm()
#     user = User.query.filter_by(username=username).first()

#     if form.is_submitted():
#         user.password_hash = User.reset_password(form.password.data)
#         db.session.commit()
#         msg= "Password reset secssefully!"
#         return render_template("reset_password.html", form=form, msg =msg)

#     return render_template("reset_password.html", form=form, msg ="")

# @users.route('/logout')
# @login_required
# def logout():
#     logout_user()
    
#     return redirect(url_for('users.home'))


# @users.route('/login', methods=['GET','POST'])
# def login():
#     form = LoginForm()
#     msg = "none"
#     if form.is_submitted():
#         user = User.query.filter_by(username=form.username.data.lower()).first()
       
#         if user == None:
#             msg = "Uncorrect email, please try again."
#             return render_template('login.html', form = form, msg = msg)
        

#         if user != None:
#             if user.check_password(form.password.data) == True:
#                 login_user(user)
#                 next = request.args.get('next')
#                 if next == None or not next[0] =='/':
#                     next = url_for('users.home')
#                 return redirect(next)
#             if user.check_password(form.password.data) == False:
#                 msg = "Uncorrect password, please try again."
#                 return render_template('login.html', form = form, msg = msg)
        
#     return render_template('login.html', form = form, msg=msg)



# @users.route('/register', methods=['POST', 'GET'])
# def register():
#     form = RegistrationForm()
#     check_email = User.query.filter_by(email=form.email.data).first()
#     check_username = User.query.filter_by(username=form.username.data).first()
#     msg = "none"
#     if form.is_submitted():

                
#         if check_email != None:
#             msg = "Email is already in use, try to login or register with another Email."
#             print(1)
#             return render_template('register.html', form= form, msg = msg)
        
#         if check_username != None:
#             msg = "Username is already in use, try to login or register with another username."
#             print(2)
#             return render_template('register.html', form= form ,msg = msg)

#         if form.password.data != form.password_confirmation.data:
#             msg = "Password and confirmation password are not the same, try again."
#             return render_template('register.html', form= form ,msg = msg)


#         if check_username == None:
#             if check_email == None:
#                 user = User(
#                     email=form.email.data.lower(),
#                     password=form.password.data,
#                     username=form.username.data.lower()
#                 )

#                 db.session.add(user)
#                 db.session.commit()
                
#                 print(3)
#                 return redirect(url_for('users.login'))

#     return render_template('register.html', form= form, msg=msg)
