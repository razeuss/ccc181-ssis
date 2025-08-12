from cloudinary.uploader import upload as cloudinary_upload
from werkzeug.utils import secure_filename

ALLOWED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/gif"}
MAX_IMAGE_SIZE = 5 * 1024 * 1024  # 5 MB

class Student:
    def __init__(self, id, firstname, lastname, program_code, year, gender, image_url):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.program_code = program_code
        self.year = year
        self.gender = gender
        self.image_url = image_url
    
    def add_student(mysql, student_id, first_name, last_name, program, year, gender, image_file):
        image_url = None

        if image_file and image_file.filename != '':
            # Check MIME type
            if image_file.mimetype not in ALLOWED_IMAGE_TYPES:
                raise ValueError("Invalid file type. Only JPG, PNG, GIF allowed.")

            # Check size
            image_file.seek(0, 2)  # go to end
            file_size = image_file.tell()
            image_file.seek(0)     # reset pointer
            if file_size > MAX_IMAGE_SIZE:
                raise ValueError("File size exceeds 5 MB.")

            # Upload to Cloudinary
            upload_result = cloudinary_upload(image_file)
            image_url = upload_result.get("secure_url")

        # If no image, store a placeholder value
        if not image_url:
            image_url = "NO_IMAGE"

        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO student (id, firstname, lastname, program_code, year, gender, image_url)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (student_id, first_name, last_name, program, year, gender, image_url))
        mysql.connection.commit()
        cur.close()
    
    def get_paginated_students(mysql, limit, offset):
        cur = mysql.connection.cursor()
        cur.execute("""
            SELECT firstname, lastname, id, program_code, gender, year, image_url 
            FROM student 
            LIMIT %s OFFSET %s
        """, (limit, offset))
        students = cur.fetchall()
        cur.close()
        return students

    def get_total_count(mysql):
        cur = mysql.connection.cursor()
        cur.execute("SELECT COUNT(*) FROM student")
        total = cur.fetchone()[0]
        cur.close()
        return total


    def get_all_students(mysql):
        cur = mysql.connection.cursor()
        cur.execute("SELECT firstname, lastname, id, program_code, gender, year, image_url FROM student")
        students = cur.fetchall()
        cur.close()
        return students
    
    def get_student_by_id(mysql, student_id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, firstname, lastname, program_code, year, gender, image_url FROM student WHERE id = %s", (student_id,))
        result = cur.fetchone()
        cur.close()
        if result:
            return Student(*result)  # Create a Student object
        return None
    
    def get_student_by_firstname(mysql, first_name):
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, firstname, lastname, program_code, year, gender, image_url FROM student WHERE firstname = %s", (first_name,))
        result = cur.fetchone()
        cur.close()
        if result:
            return Student(*result)  # Create a Student object
        return None
    
    def get_student_by_lastname(mysql, last_name):
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, firstname, lastname, program_code, year, gender, image_url FROM student WHERE lastname = %s", (last_name,))
        result = cur.fetchone()
        cur.close()
        if result:
            return Student(*result)  # Create a Student object
        return None
   
    @staticmethod
    def update_student(mysql, student_id, first_name, last_name, program, year, gender, image_file=None):
        image_url = None
        if image_file:
            upload_result = cloudinary_upload(image_file)
            image_url = upload_result.get("secure_url")
        
        cur = mysql.connection.cursor()
        
        if image_url:
            cur.execute("""
                UPDATE student 
                SET firstname = %s, lastname = %s, program_code = %s, year = %s, gender = %s, image_url = %s
                WHERE id = %s
            """, (first_name, last_name, program, year, gender, image_url, student_id))
        else:
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