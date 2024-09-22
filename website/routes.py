from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

views = Blueprint('views', __name__)
mysql = MySQL()


views = Blueprint('views', __name__)

@views.route('/')
def homepage():
    return render_template("Master Layout/homepage.html")


@views.route('/add', methods=['GET', 'POST'])
def addstud():
    if request.method == 'POST':
       
        student_id = request.form['studentID']
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        program = request.form['program']
        year = request.form['year']
        gender = request.form['gender']

     
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO student (id, firstname, lastname, program_code, year, gender) VALUES (%s, %s, %s, %s, %s, %s)", 
                    (student_id, first_name, last_name, program, year, gender))
        mysql.connection.commit()
        cur.close()

        flash('Student Added Successfully', 'success')
        return redirect(url_for('views.students_list'))

    return render_template("Student Layout/studentslist.html")


@views.route('/Students')
def students_list():
    cur = mysql.connection.cursor()
    
    cur.execute("SELECT firstname, lastname, id, program_code, gender, year FROM student")
    students = cur.fetchall()  
    cur.close()

   
    return render_template('Student Layout/studentslist.html', students=students)



@views.route('/programs')
def update():
    cur = mysql.connection.cursor()
   
    cur.execute("SELECT code, name, college_code FROM program")
    programs = cur.fetchall() 
    cur.close()

    
    return render_template('Program layout/programs.html', programs=programs)



@views.route('/add_program', methods=['GET', 'POST'])
def add_program():
    if request.method == 'POST':
       
        coursecode = request.form['programcode']
        coursename = request.form['programname']
        collegecode = request.form['collegecode']
        

     
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO program (code, name, college_code) VALUES (%s, %s, %s)", 
                    (coursecode, coursename, collegecode))
        mysql.connection.commit()
        cur.close()

        flash('Program Added Successfully', 'success')
        return redirect(url_for('views.update'))
    
    return render_template("Program layout/programs.html")


@views.route('/add_college', methods=['GET', 'POST'])
def add_college():
    if request.method == 'POST':
       
        collegecode = request.form['programname']
        collegename = request.form['collegecode']
        

     
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO college (code, name) VALUES (%s, %s)", 
                    (collegecode, collegename))
        mysql.connection.commit()
        cur.close()

        flash('Program Added Successfully', 'success')
        return redirect(url_for('views.college'))
    
    return render_template("College Layout/college.html")
    
@views.route('/college')
def college():
    cur = mysql.connection.cursor()
   
    cur.execute("SELECT code, name FROM college")
    colleges = cur.fetchall() 
    cur.close()

    
    return render_template('College Layout/college.html', colleges=colleges)

