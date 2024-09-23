from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

views = Blueprint('views', __name__)
mysql = MySQL()


@views.route('/')
def homepage():
    return render_template("Master Template/homepage.html")

