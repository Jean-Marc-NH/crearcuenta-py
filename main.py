"""
Proyecto:
- Abrir asistente
- Login o registro
- regitro va a crear un usuario en la bd
- login lo va a identificar 
- despues preguntara si queremos crear, una nota mostrarlas o borrarlas
"""
from os import system
import dependencias.cuenta as c
import dependencias.interfaz as i

cuenta = c.cuenta("localhost", "root", "project_001")
interfaz = i.interfaz(cuenta)

# Interfaz

interfaz.pantalla_principal()