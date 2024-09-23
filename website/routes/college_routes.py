from flask import Blueprint, render_template, request, redirect, url_for, flash
from website.models.college import College
from website import MySQL

college_bp = Blueprint('college_bp', __name__)
mysql = MySQL()

@college_bp.route('/add', methods=['GET', 'POST'])
def add_college():
    if request.method == 'POST':
        code = request.form['collegecode']
        name = request.form['collegename']

        College.add_college(mysql, code, name)
        flash('College Added Successfully', 'success')
        return redirect(url_for('college_bp.colleges_list'))

    return render_template("College Template/college.html")

@college_bp.route('/college')
def colleges_list():
    colleges = College.get_all_colleges(mysql)
    return render_template('College Template/college.html', colleges=colleges)