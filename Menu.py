import os

def menuMain():
    while True:
        print("-----------------Menu Principal------------------------")
        print("|                                                     |")
        print("| 1.Crear AFD                                         |")
        print("| 2.Crear Gramatica                                   |")
        print("| 3.Evauluar Cadena                                   |")
        print("| 4.Reportes                                          |")
        print("| 5.Cargar Archivo de Entrada                         |")
        print("|   SALIR                                             |")
        print("|                                                     |")
        print("-------------------------------------------------------")
        print("")
        print(">> ",end="")
        opcion = input()
        opcion = opcion.strip()
        if opcion == "1":
            os.system("cls")
            menuAFD()
        elif opcion == "2":
            pass
        elif opcion =="3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        elif opcion.lower() == "salir":
            break

def menuAFD():
    print("Hola Menu AFD")