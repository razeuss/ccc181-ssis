from flask import Blueprint, render_template, request, redirect, url_for, flash, get_flashed_messages
from website.models.student import Student
from website.models.programs import Program
from flask_mysqldb import MySQL
from flask import jsonify

student_bp = Blueprint('student_bp', __name__)
mysql = MySQL()

@student_bp.route('/add', methods=['GET', 'POST'])
def addstud():
    if request.method == 'POST':
        student_id = request.form['studentID']
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        program = request.form['program']
        year = request.form['year']
        gender = request.form['gender']
        image_file = request.files['image']

        existing_student = Student.get_student_by_id(mysql, student_id)
        if existing_student:
            flash('Student ID already exists. Please use a unique ID.', 'error')
            return redirect(url_for('student_bp.students_list'))

        program_exists = Program.search_program(mysql, program)
        if not program_exists:
            flash('The program does not exist. Please choose a valid program.', 'error')
            return redirect(url_for('student_bp.students_list'))

        Student.add_student(mysql, student_id, first_name, last_name, program, year, gender, image_file)
        flash('Student Added Successfully', 'success')
        return redirect(url_for('student_bp.students_list'))

    return render_template("Student Template/studentslist.html")



@student_bp.route('/Students')
def students_list():
    
    page = int(request.args.get('page', 1))
    per_page = 50
    offset = (page - 1) * per_page

    
    students = Student.get_paginated_students(mysql, per_page, offset)

   
    total_students = Student.get_total_count(mysql)
    total_pages = (total_students + per_page - 1) // per_page

    return render_template(
        'Student Template/studentslist.html',
        students=students,
        page=page,
        total_pages=total_pages
    )


@student_bp.route('/student', methods=['GET'])
def get_student():
    query = request.args.get('query')
    student = Student.get_student_by_id(mysql, query) or Student.get_student_by_firstname(mysql, query) or Student.get_student_by_lastname(mysql, query)
    if student:
        return jsonify({
            'firstname': student.firstname,
            'lastname': student.lastname,
            'id': student.id,
            'program_code': student.program_code,
            'gender': student.gender,
            'year': student.year,
            'image_url': student.image_url
        })
    return jsonify(None), 404


@student_bp.route('/edit/<string:student_id>', methods=['GET', 'POST'])
def update_student(student_id):
    student = Student.get_student_by_id(mysql, student_id)
    if not student:
        flash('Student not found', 'error')
        return redirect(url_for('student_bp.students_list'))

    if request.method == 'POST':
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        program = request.form['program']
        year = request.form['year']
        gender = request.form['gender']
        image_file = request.files['updateprofile']

        program_exists = Program.search_program(mysql, program)
        if not program_exists:
            flash('The program does not exist. Please choose a valid program.', 'error')
            return redirect(url_for('student_bp.students_list'))

        Student.update_student(mysql, student_id, first_name, last_name, program, year, gender, image_file)
        flash('Student Updated Successfully', 'success')
        return redirect(url_for('student_bp.students_list'))

    return render_template('Student Template/studentslist.html', student=student)


@student_bp.route('/delete/<string:student_id>', methods=['POST'])
def delete_student(student_id):
    student = Student.get_student_by_id(mysql, student_id)
    if not student:
        flash('Student not found', 'error')
        return redirect(url_for('student_bp.students_list'))

    Student.delete_student(mysql, student_id)
    flash('Student Deleted Successfully', 'success')
    return redirect(url_for('student_bp.students_list'))
