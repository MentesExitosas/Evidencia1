import os
import shutil

print("Bienvenido al clonador de archivos")
print("Selecciona una opción:\n 1. Ver en que directorio estoy\n 2. Clonar un archivo de un directorio a otro\n")
opcion = int(input("Opción: "))

if opcion == 1:
    print(f"El directorio de trabajo actual es: {os.getcwd()}")
elif opcion == 2:
    directorioInicial = input("Dime la ruta del directorio donde se encuentra el archivo que quieres copiar:\n")
    directorioFinal = input("Dime la ruta de a donde se va a copiar el archivo:\n")
    shutil.copy(directorioInicial, directorioFinal)
elif opcion == 3:
    directorioInicial = input("Dime la ruta del directorio donde se encuentra el archivo que quiere mover:\n")
    directorioFinal = input("Dime la ruta de a donde se va a mover el archivo:\n")
    shutil.move(directorioInicial, directorioFinal)