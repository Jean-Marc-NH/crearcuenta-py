"""
Proyecto:
- Abrir asistente
- Login o registro
- regitro va a crear un usuario en la bd
- login lo va a identificar 
- despues preguntara si queremos crear, una nota mostrarlas o borrarlas
"""
from os import system
import cuenta as c

cuenta = c.cuenta()

# Interfaz

while True:
    
    system("cls")
    print("----- Inicio -----")
    print("[1] login")
    print("[2] register")

    x = input("ingrese su opcion")

    if(x == '1'):
        system("cls")
        print("----- Login -----")
        cuenta.login()
        break

    elif(x == '2'):
        print("----- Registro -----")
        system("cls")
        cuenta.registro()
        break

    else:
        print("ingrese un valor correcto")