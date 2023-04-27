import mysql.connector as sql

class cuenta:

    def __init__(self):
        self.password = None
        self.fecha = None
        self.email = None
        self.nombre = None
        self.apellidos = None

        self.dataBase = sql.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "project_001"
        )

        self.cursor = self.dataBase.cursor()


    def login(self):
        self.email = input("Ingrese su e-mail: ")
        self.password = input("Ingrese su contraseña: ")

        self.cursor.execute("SELECT * FROM usuarios")
        usuarios =  self.cursor.fetchall()

        for x in usuarios:
            print(x)

            if(self.email == x[3]):
                if(self.password == x[4] ):
                    return True
            
            return False
    
    def registro(self):

        while True:
            try:
                self.nombre = input("Ingrese su nombre: ")
                self.apellidos = input("Ingrese sus apellidos: ")
                self.email = input("Ingrese su e-mail: ")
                self.password = input("Ingrese su contraseña: ")
                self.fecha = input("Ingrese su fecha de nacimiento: ")

                self.cursor.execute("INSERT INTO usuarios VALUE(null, '" + 
                self.nombre + "', '"+ self.apellidos + "', '" + self.email +
                "', '" + self.password + "', '" + self.fecha +"')")

                self.dataBase.commit()

                break
            except:
                print("Correo ya existente")
                continue
        
