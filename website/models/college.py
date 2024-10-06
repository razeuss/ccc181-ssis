class College:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    @staticmethod
    def add_college(mysql, code, name):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO college (code, name) VALUES (%s, %s)", (code, name))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def get_all_colleges(mysql):
        cur = mysql.connection.cursor()
        cur.execute("SELECT code, name FROM college")
        colleges = cur.fetchall()
        cur.close()
        return colleges

    @staticmethod
    def get_college_by_code(mysql, code):
        cur = mysql.connection.cursor()
        cur.execute("SELECT code, name FROM college WHERE code = %s", (code,))
        college = cur.fetchone()
        cur.close()
        return college

    @staticmethod
    def get_college_by_name(mysql, name):
        cur = mysql.connection.cursor()
        cur.execute("SELECT code, name FROM college WHERE name = %s", (name,))
        college = cur.fetchone()
        cur.close()
        return college


    @staticmethod
    def update_college(mysql, old_code, new_code, name):
        cur = mysql.connection.cursor()
        cur.execute("UPDATE college SET code = %s, name = %s WHERE code = %s", 
                    (new_code, name, old_code))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def delete_college(mysql, code):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM college WHERE code = %s", (code,))
        mysql.connection.commit()
        cur.close()
