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

        existing_student = Student.get_student_by_id(mysql, student_id)
        if existing_student:
            flash('Student ID already exists. Please use a unique ID.', 'error')
            return redirect(url_for('student_bp.students_list'))

        program_exists = Program.search_program(mysql, program)
        if not program_exists:
            flash('The program does not exist. Please choose a valid program.', 'error')
            return redirect(url_for('student_bp.students_list'))

        Student.add_student(mysql, student_id, first_name, last_name, program, year, gender)
        flash('Student Added Successfully', 'success')
        return redirect(url_for('student_bp.students_list'))

    return render_template("Student Template/studentslist.html")



@student_bp.route('/Students')
def students_list():
    students = Student.get_all_students(mysql)
    return render_template('Student Template/studentslist.html', students=students)

@student_bp.route('/student', methods=['GET'])
def get_student():
    query = request.args.get('query')
    
    student_id = Student.get_student_by_id(mysql, query)
    if student_id:
        return jsonify({
            'firstname': student_id.firstname,
            'lastname': student_id.lastname,
            'id': student_id.id,
            'program_code': student_id.program_code,
            'gender': student_id.gender,
            'year': student_id.year
        })
    
    student_firstname= Student.get_student_by_firstname(mysql, query)
    if student_firstname:
        return jsonify({
            'firstname': student_firstname.firstname,
            'lastname': student_firstname.lastname,
            'id': student_firstname.id,
            'program_code': student_firstname.program_code,
            'gender': student_firstname.gender,
            'year': student_firstname.year
        })
    student_lastname= Student.get_student_by_lastname(mysql, query)
    if student_lastname:
        return jsonify({
            'firstname': student_lastname.firstname,
            'lastname': student_lastname.lastname,
            'id': student_lastname.id,
            'program_code': student_lastname.program_code,
            'gender': student_lastname.gender,
            'year': student_lastname.year
        })
    return jsonify(None)


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

        program_exists = Program.search_program(mysql, program)
        if not program_exists:
            flash('The program does not exist. Please choose a valid program.', 'error')
            return redirect(url_for('student_bp.students_list'))

        Student.update_student(mysql, student_id, first_name, last_name, program, year, gender)
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
