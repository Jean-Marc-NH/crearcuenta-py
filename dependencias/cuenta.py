import hashlib

class cuenta:

    def __init__(self, cursor, dataBase):
        self.password = None
        self.fecha = None
        self.email = None
        self.nombre = None
        self.apellidos = None

        self.dataBase = dataBase
        self.cursor = cursor


    def login(self):
        self.email = input("Ingrese su e-mail: ")
        self.password = input("Ingrese su contraseña: ")

        self.cursor.execute("SELECT * FROM usuarios")
        usuarios =  self.cursor.fetchall()

        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode("utf8"))

        for x in usuarios:
            if(self.email == x[3] and cifrado.hexdigest() == x[4]):
                return x[0]
            
        return False
    
    def registro(self):

        while True:
            try:
                self.nombre = input("Ingrese su nombre: ")
                self.apellidos = input("Ingrese sus apellidos: ")
                self.email = input("Ingrese su e-mail: ")
                self.password = input("Ingrese su contraseña: ")
                self.fecha = input("Ingrese su fecha de nacimiento: ")

                cifrado = hashlib.sha256()
                cifrado.update(self.password.encode("utf8"))

                self.cursor.execute("INSERT INTO usuarios VALUE(null, '" + 
                self.nombre + "', '"+ self.apellidos + "', '" + self.email +
                "', '" + cifrado.hexdigest() + "', '" + self.fecha +"')")

                self.dataBase.commit()

                break
            except:
                print("Correo ya existente")
                continue
        
