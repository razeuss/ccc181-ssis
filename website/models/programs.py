class Program:
    def __init__(self, code, name, college_code):
        self.code = code
        self.name = name
        self.college_code = college_code

    @staticmethod
    def add_program(mysql, code, name, college_code):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO program (code, name, college_code) VALUES (%s, %s, %s)", 
                    (code, name, college_code))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def get_all_programs(mysql):
        cur = mysql.connection.cursor()
        cur.execute("SELECT code, name, college_code FROM program")
        programs = cur.fetchall()
        cur.close()
        return programs


    @staticmethod
    def update_program(mysql, old_code, new_code, name, college_code):
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE program 
            SET code = %s, name = %s, college_code = %s 
            WHERE code = %s
        """, (new_code, name, college_code, old_code))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def delete_program(mysql, code):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM program WHERE code = %s", (code,))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def search_program(mysql, code):
        cur = mysql.connection.cursor()
        cur.execute("SELECT code, name, college_code FROM program WHERE code = %s", (code,))
        program = cur.fetchone()  
        cur.close()
        if program:
            return Program(*program) 
        return None

    @staticmethod
    def filter_programs(mysql, college_code):
        cur = mysql.connection.cursor()
        cur.execute("SELECT code, name, college_code FROM program WHERE college_code = %s", (college_code,))
        programs = cur.fetchall()
        cur.close()
        return programs
    
    @staticmethod
    def get_program_by_code(mysql, code):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM program WHERE code = %s", (code,))
        program = cur.fetchone()
        cur.close()
        return program
    
    @staticmethod
    def search_program_by_name(mysql, name):
        cur = mysql.connection.cursor()
        cur.execute("SELECT code, name, college_code FROM program WHERE name = %s", (name,))
        program = cur.fetchone()  
        cur.close()
        return program
    
    
