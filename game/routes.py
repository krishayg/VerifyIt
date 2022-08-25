from game import app
from flask import render_template, redirect,url_for, flash, request
#from game.models import
#from game.forms import
from game import db
from flask_login import login_user,logout_user, login_required, current_user
@app.route("/")
@app.route("/home")
def home_page():
    return render_template("base.html")