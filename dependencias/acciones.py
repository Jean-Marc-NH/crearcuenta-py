from datetime import datetime

class nota:

    def __init__(self, id, cursor, dataBase):
        self.usuario_id = id
        self.titulo = None
        self.nota = None

        self.cursor = cursor
        self.dataBase = dataBase

    def crear_nota(self):

        while True:
            try:
                self.titulo = input("Ingrese un titulo para su nota: ")
                self.nota = input("escriba el contenido de su nota: \n")

                self.cursor.execute("INSERT INTO notas VALUE(null, '" + 
                str(self.usuario_id) + "', '"+ self.titulo + "', '" + self.nota +
                "', NOW())")       

                self.dataBase.commit()

                break

            except:
                print("\nElija otro titulo")

    def leer_nota(self):

        self.cursor.execute("SELECT * FROM notas")
        notas =  self.cursor.fetchall()
        data = []

        i = 0

        for x in notas:
            i += 1
            if(self.usuario_id == x[1]):
                print( "[ {} ]".format(i) , x[2])
                data.append(x)

        if(i > 0):
            tmp = input("ingrese el titulo que desea leer: ")

            for x in data:
                if(x[2] == tmp):
                    print(x[3], "\n Fecha: ", x[4], "\n")


        else:
            print("No hay notas") 