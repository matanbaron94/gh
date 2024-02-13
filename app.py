from Crow_app import db, app, new_gallery
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user, current_user

from werkzeug.security import generate_password_hash,check_password_hash
import os









if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)