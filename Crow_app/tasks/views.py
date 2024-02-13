
from Crow_app import db
from flask import render_template, redirect, request, url_for, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from Crow_app.models import Task
from Crow_app.tasks.forms import NewTask
from werkzeug.security import generate_password_hash,check_password_hash
import os


tasksr = Blueprint('tasks', __name__)


@tasksr.route('/delete/<id>', methods=['POST','GET'])
@login_required
def delete_task(id):
        print("sdfsdfs")
        print(id)
        task = Task.query.filter_by(id=id).first()
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('tasks.tasks'))



@tasksr.route('/task-done/<id>', methods=['POST','GET'])
@login_required
def task_done(id):
        print("sdfsdfs")
        print(id)
        task = Task.query.filter_by(id=id).first()
        task.status = "Done"
        
        db.session.commit()
        return redirect(url_for('tasks.tasks'))


@tasksr.route('/task-waiting/<id>', methods=['POST','GET'])
@login_required
def task_waiting(id):
        print("666")
        print(id)
        task = Task.query.filter_by(id=id).first()
        task.status = "Waiting"
        
        db.session.commit()
        return redirect(url_for('tasks.tasks'))





@tasksr.route("/my-tasks",methods=['GET','POST'])
@login_required
def tasks():
    form = NewTask()
    u = current_user
    user_tasks = Task.query.filter_by(user=u.id)
    
    if form.is_submitted():
        new_task = Task(user_id=form.user_id.data,task=form.task.data,status="Waiting")
        db.session.add(new_task)
        db.session.commit()
        return render_template("tasks.html", form=form,user_tasks=user_tasks )
    return render_template("tasks.html", form=form, user_tasks=user_tasks)