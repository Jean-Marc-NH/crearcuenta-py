from os import system
import dependencias.cuenta as cu
import dependencias.conexion as co
import dependencias.acciones as ac

class interfaz: 
    def __init__(self , host, user, db, pwd=""):
        self.conexion = co.conexion(host, user, db, pwd)
        self.cuenta = cu.cuenta(self.conexion.get_cursor(), self.conexion.get_dataBase())
        self.user_id = None

    def pantalla_principal(self):
        while True:
    
            system("cls")
            print("----- Inicio -----")
            print("[1] login")
            print("[2] register")
            print("[otro] Salir")

            x = input("ingrese su opcion: ")

            if(x == '1'):
                system("cls")
                print("----- Login -----")
                self.user_id =  self.cuenta.login()
                print(self.user_id)
                if(self.user_id != False):
                    return True

            
            elif(x == '2'):
                print("----- Registro -----")
                system("cls")
                self.cuenta.registro()
            
            else:
                return False

    def pantalla_notas(self):

        notas = ac.nota(self.user_id, self.conexion.get_cursor(), self.conexion.get_dataBase())
    
        while True:
    
    
            print("----- Notas -----")
            print("[1] Crear Nota")
            print("[2] Ver Notas")
            print("[3] Borrar Notas")
            print("[otro] Salir")

            x = input("ingrese su opcion: ")

            if(x == '1'):
                system("cls")
                print("----- crear nota -----")

                notas.crear_nota()
                print("\nNOTA CREADA !!!")
            
            elif(x == '2'):
                print("----- Ver Notas -----")
                system("cls")
                
                notas.leer_nota()

            else:
                break


class programa:
    def __init__(self):
        self.ejecucion = interfaz("localhost", "root", "project_001")

        if(self.ejecucion.pantalla_principal() == True):
            self.ejecucion.pantalla_notas()
        else:
            system("cls")
            print("cerro el programa")