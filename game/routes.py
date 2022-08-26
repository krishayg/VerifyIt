from game import app
from flask import render_template, redirect,url_for, flash, request
#from game.models import
from game.forms import JoinForm
from game import db
from flask_login import login_user,logout_user, login_required, current_user
@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")
@app.route("/join",methods=["GET","POST"])
def join_page():
    form=JoinForm()
    if form.submit.data and form.validate():
        newlink="/waiting/"+str(form.code.data)
        return redirect(newlink)
    return render_template("join.html",form=form)
@app.route("/waiting/<id>")
def waiting_page(id):
    return render_template("waitscreenplayer.html")