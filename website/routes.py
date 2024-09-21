from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

views = Blueprint('views', __name__)
mysql = MySQL()


views = Blueprint('views', __name__)

@views.route('/')
def homepage():
    return render_template("homepage.html")

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

    return render_template("studentslist.html")

@views.route('/programs')
def update():
    return render_template("programs.html")

@views.route('/Students')
def students_list():
    cur = mysql.connection.cursor()
    # Query to fetch all students
    cur.execute("SELECT firstname, lastname, id, program_code, gender, year FROM student")
    students = cur.fetchall()  # Fetch all rows from the query result
    cur.close()

    # Pass the 'students' list to the template
    return render_template('studentslist.html', students=students)

