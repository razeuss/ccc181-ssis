from flask import Blueprint, render_template, request, redirect, url_for, flash
from website.models.college import College
from website import MySQL
from flask import jsonify

college_bp = Blueprint('college_bp', __name__)
mysql = MySQL()

@college_bp.route('/addcollege', methods=['GET', 'POST'])
def add_college():
    if request.method == 'POST':
        code = request.form['collegecode']
        name = request.form['collegename']

        existing_college = College.get_college_by_code(mysql, code)
        if existing_college:
            flash('College already exists.', 'error')
            return redirect(url_for('college_bp.colleges_list'))

       
        College.add_college(mysql, code, name)
        flash('College Added Successfully', 'success')
        return redirect(url_for('college_bp.colleges_list'))

    return render_template("College Template/college.html")

@college_bp.route('/college')
def colleges_list():
    colleges = College.get_all_colleges(mysql)
    return render_template('College Template/college.html', colleges=colleges)

@college_bp.route('/search_college', methods=['GET'])
def search_college():
    query = request.args.get('query', '').strip()
    cur = mysql.connection.cursor()

    # Match by code or name (case-insensitive partial search)
    cur.execute("""
        SELECT code, name
        FROM college
        WHERE code LIKE %s OR name LIKE %s
    """, (f"%{query}%", f"%{query}%"))

    colleges = cur.fetchall()
    cur.close()

    return jsonify([
        {"code": c[0], "name": c[1]} for c in colleges
    ])



@college_bp.route('/updatecollege/<string:code>', methods=['GET', 'POST'])
def update_college(code):
    if request.method == 'POST':
        new_code = request.form['collegecode']
        name = request.form['collegename']
        
        College.update_college(mysql, code, new_code, name)
        flash('College Updated Successfully', 'success')
        return redirect(url_for('college_bp.colleges_list'))

    return redirect(url_for('college_bp.colleges_list'))

@college_bp.route('/deletecollege/<string:code>', methods=['POST'])
def delete_college(code):
    College.delete_college(mysql, code)
    flash('College Deleted Successfully', 'success')
    return redirect(url_for('college_bp.colleges_list'))









