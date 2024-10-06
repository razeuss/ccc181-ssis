class Student:
    def __init__(self, id, firstname, lastname, program_code, year, gender):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.program_code = program_code
        self.year = year
        self.gender = gender

    def add_student(mysql, student_id, first_name, last_name, program, year, gender):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO student (id, firstname, lastname, program_code, year, gender) VALUES (%s, %s, %s, %s, %s, %s)", 
                    (student_id, first_name, last_name, program, year, gender))
        mysql.connection.commit()
        cur.close()

    def get_all_students(mysql):
        cur = mysql.connection.cursor()
        cur.execute("SELECT firstname, lastname, id, program_code, gender, year FROM student")
        students = cur.fetchall()
        cur.close()
        return students
    
    def get_student_by_id(mysql, student_id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM student WHERE id = %s", (student_id,))
        result = cur.fetchone()
        cur.close()
        if result:
            return Student(*result) 
        return None
    
    def get_student_by_firstname(mysql, first_name):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM student WHERE firstname = %s", (first_name,))
        result = cur.fetchone()
        cur.close()
        if result:
            return Student(*result) 
        return None
    
    def get_student_by_lastname(mysql, last_name):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM student WHERE lastname = %s", (last_name,))
        result = cur.fetchone()
        cur.close()
        if result:
            return Student(*result) 
        return None
   
    def update_student(mysql, student_id, first_name, last_name, program, year, gender):
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE student 
            SET firstname = %s, lastname = %s, program_code = %s, year = %s, gender = %s 
            WHERE id = %s
        """, (first_name, last_name, program, year, gender, student_id))
        mysql.connection.commit()
        cur.close()
        
    def delete_student(mysql, student_id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM student WHERE id = %s", (student_id,))
        mysql.connection.commit()
        cur.close()