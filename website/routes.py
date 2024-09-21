from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def homepage():
    return render_template("homepage.html")

@views.route('/add')
def addstud():
    return render_template("addstud.html")

@views.route('/programs')
def update():
    return render_template("programs.html")

@views.route('/Students')
def students_list():
    return render_template("studentslist.html")
