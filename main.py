import os
import shutil

print("Bienvenido al clonador de archivos")
print("Selecciona una opción:\n 1. Ver en que directorio estoy\n 2. Clonar un archivo de un directorio a otro\n")
opcion = int(input("Opción: "))

if opcion == 1:
    print(f"El directorio de trabajo actual es: {os.getcwd()}")