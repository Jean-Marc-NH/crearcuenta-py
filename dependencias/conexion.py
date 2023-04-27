import mysql.connector as sql

class conexion:

    def __init__(self, host, user, db, pwd=""):
        
        self.dataBase = sql.connect(
            host = host,
            user = user,
            passwd = pwd,
            database = db
        )

        self.cursor = self.dataBase.cursor(buffered=True)

    def get_cursor(self):
        return self.cursor
    
    def get_dataBase(self):
        return self.dataBase

