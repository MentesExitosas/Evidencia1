import os
import sys
import shutil

listaVacia = []

opcion = 1
while opcion >= 1 and opcion <5:

    print("Bienvenido al clonador de archivos y organizador de listas y tuplas\n")
    print("Selecciona una opción:\n 1. Ver en que directorio estoy\n 2. Clonar un archivo o directorio a otro lugar\n 3. Mover un archivo o directorio a otro lugar\n 4. Listas\n 5. Salir")
    opcion = int(input("\nOpción: "))


    try:
        if opcion == 1:
            print(f"\nEl directorio de trabajo actual es: {os.getcwd()}")
            print(f"El peso del objeto es: {sys.getsizeof(os.getcwd())} bytes")
        elif opcion == 2:
            directorioInicial = input("\nDime la ruta del directorio donde se encuentra el archivo que quieres copiar: \n")
            directorioFinal = input("Dime la ruta de a donde se va a copiar el archivo: \n")
            shutil.copy(directorioInicial, directorioFinal)
            print(f"El peso del objeto es: {sys.getsizeof(directorioInicial)} bytes")
        elif opcion == 3:
            directorioInicial = input("\nDime la ruta del directorio donde se encuentra el archivo que quiere mover: \n")
            directorioFinal = input("Dime la ruta de a donde se va a mover el archivo: \n")
            shutil.move(directorioInicial, directorioFinal)
            print(f"El peso del objeto es: {sys.getsizeof(directorioInicial)} bytes")
        elif opcion == 4:
            elementosLista = int(input('\n¿Cuántos elementos desea agregar? '))
            for elemento in range(elementosLista):
                elementosLista = (input('¿Cuáles valores vas a agregar?  '))
                listaVacia.append(elementosLista)
            print("\nLISTA TERMINADA")
            print(listaVacia)
            print('\nSelecciona una opcion:\n 1. Saber la posición de un elemento en la lista\n 2. Inserta un elemento en la lista según el índice deseado\n 3. Eliminar elemento de la lista\n 4. Ejecutar la función pop en la lista\n 5. Ordenar los elementos de la lista utilizando sort \n 6. Verificar cuantas veces se repite un valor de la lista')
            opcionsub = int(input(' \nSeleccion SubMenu de Listas: '))
            if opcionsub == 1:
                print(listaVacia)
                opcionindex = input('\n¿De cuál elemento de la lista desea saber su posicion? ')
                print(f'La posicion del elemento es: {listaVacia.index(opcionindex)}')
            if opcionsub == 2:
                print(listaVacia)
                opcioninsertnumero = int(input('\n¿En qué posicion desea agregar? '))
                opcioninsertelemento = input('¿Cuál elemento deseas agregar? ')
                listaVacia.insert(opcioninsertnumero, opcioninsertelemento)   
                print(listaVacia) 
            if opcionsub == 3:
                print(listaVacia)
                opcionremoveelemento = input('\nEscriba el elemento a eliminar: ')
                listaVacia.remove(opcionremoveelemento)
                print(listaVacia)
            if opcionsub ==4:
                print("\n")
                print(listaVacia)
                print(f"El elemento a eliminar es: {listaVacia.pop()}")
                print(f"La lista actualizada es: {listaVacia}")
            if opcionsub ==5:
                print("\n")
                print(listaVacia)
                listaVacia.sort()
                print(f"La lista ordenada es: {listaVacia}")
            if opcionsub == 6:
                print("\n")
                print(listaVacia)
                valorCount = input("¿Qué valor deseas saber cuantas veces se repite en la lista? \n")
                print(f"El valor {valorCount} se repite {listaVacia.count(valorCount)} veces")
            print('Se convertirá la lista a tupla: ')
            tupla = tuple(listaVacia)
            print(f' El peso de la lista {listaVacia} es: {sys.getsizeof(listaVacia)} bytes y el peso de la tupla {tupla} es: {sys.getsizeof(tupla)} bytes')
    except Exception:   
        print(f"Ocurrió un error {sys.exc_info()[0]}")
