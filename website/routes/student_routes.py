from flask import Blueprint, render_template, request, redirect, url_for, flash
from website.models.student import Student
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

      
        Student.add_student(mysql, student_id, first_name, last_name, program, year, gender)
        flash('Student Added Successfully', 'success')
        return redirect(url_for('student_bp.students_list'))

    return render_template("Student Template/studentslist.html")


@student_bp.route('/Students')
def students_list():
    students = Student.get_all_students(mysql)
    return render_template('Student Template/studentslist.html', students=students)

@student_bp.route('/student/<string:student_id>')
def get_student(student_id):
    student = Student.get_student_by_id(mysql, student_id)
    if student:
        return jsonify({
            'firstname': student.firstname,
            'lastname': student.lastname,
            'id': student.id,
            'program_code': student.program_code,
            'gender': student.gender,
            'year': student.year
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

        # Update student information in the database
        Student.update_student(mysql, student_id, first_name, last_name, program, year, gender)
        flash('Student Updated Successfully', 'success')
        return redirect(url_for('student_bp.students_list'))
    
    return render_template('Student Template/studentslist.html', student=student)