import os
import sys
import shutil

listavacia = []
print("Bienvenido al clonador de archivos")
print("Selecciona una opción:\n 1. Ver en que directorio estoy\n 2. Clonar un archivo o directorio a otro lugar\n 3. Mover un archivo o directorio a otro lugar\n 4. Listas\n 5. Tuplas")
opcion = int(input("Opción: "))


try:
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
    elif opcion == 4:
        print('Selecciona una opcion:\n 1.Agregar Valores a Lista\n 2.Saber posicion de un elemento en la lista\n 3.Inserta un elemento en la lista según el indicie deseado ')
        opcionsub = int(input(' Seleccion SubMenu de Listas: '))
        if opcionsub == 1:
            elementoslista = int(input('Cuantos elementos desea agregar: '))
            for elemento in range(elementoslista + 1):
                numeroslista = int(input('Cuales numeros vas a agregar? : '))
                listavacia.append(numeroslista)
            print(listavacia)
        
except Exception:
    print(f"Ocurrió un error {sys.exc_info()[0]}")
else:
    print("Valor Erróneo")
