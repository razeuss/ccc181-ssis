class College:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    @staticmethod
    def add_college(mysql, code, name):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO college (code, name) VALUES (%s, %s)", 
                    (code, name))
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def get_all_colleges(mysql):
        cur = mysql.connection.cursor()
        cur.execute("SELECT code, name FROM college")
        colleges = cur.fetchall()
        cur.close()
        return colleges