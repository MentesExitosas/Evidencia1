import os
import sys
import shutil

listaVacia = []
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
        elementosLista = int(input('Cuantos elementos desea agregar: '))
        for elemento in range(elementosLista):
            elementosLista = (input('Cuales numeros vas a agregar? : '))
            listaVacia.append(elementosLista)
        print(listaVacia)
        print('Selecciona una opcion:\n 1.Saber posicion de un elemento en la lista\n 2.Inserta un elemento en la lista según el indicie deseado\n 3.Eliminar elemento de la lista ')
        opcionsub = int(input(' Seleccion SubMenu de Listas: '))
        if opcionsub == 1:
            print(listaVacia)
            opcionindex = input('De cual elemento de la lista desea saber su posicion :')
            print(f'La posicion del elemento es : {listaVacia.index(opcionindex)}')
        if opcionsub == 2:
            print(listaVacia)
            opcioninsertnumero = int(input('En que posicion desea agregar : '))
            opcioninsertelemento = input('Cual elemento deseas agregar : ')
            listaVacia.insert(opcioninsertnumero, opcioninsertelemento)   
            print(listaVacia) 
        if opcionsub == 3:
            print(listaVacia)
            opcionremoveelemento = input('Escriba el elemento a eliminar: ')
            listaVacia.remove(opcionremoveelemento)
            print(listaVacia)
except Exception:
    print(f"Ocurrió un error {sys.exc_info()[0]}")
