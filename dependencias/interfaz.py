from os import system

class interfaz: 
    def __init__(self, cuenta) -> None:
        self.cuenta = cuenta

    def pantalla_principal(self):
        while True:
    
            system("cls")
            print("----- Inicio -----")
            print("[1] login")
            print("[2] register")

            x = input("ingrese su opcion")

            if(x == '1'):
                system("cls")
                print("----- Login -----")
                if(self.cuenta.login()):
                    print("Entraste")
                break
            
            elif(x == '2'):
                print("----- Registro -----")
                system("cls")
                self.cuenta.registro()
                break
            
            else:
                print("ingrese un valor correcto")