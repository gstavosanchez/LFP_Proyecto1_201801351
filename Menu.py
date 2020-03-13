import os
import ManejadorAFD
def menuMain():
    while True:
        print("-------------------Menu Principal----------------------")
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
        else:
            os.system("cls")

def setNombreAFD():
    print("Ingrese el nombre de AFD")
    print(">> ",end="")
    nombre = input()
    nombre = nombre.strip()
    os.system("cls")
    return nombre


def menuAFD():
    nombre = setNombreAFD()
    if nombre != "update":
        if ManejadorAFD.newAFD(nombre) == True:
            while True:
                print("-----------------------Menu AFD------------------------")
                print("|                                                     |")
                print("| 1.Ingresar Estados                                  |")
                print("| 2.Ingresar Alfabeto                                 |")
                print("| 3.Estado Inicial                                    |")
                print("| 4.Estado Aceptacion                                 |")
                print("| 5.Transiciones                                      |")
                print("| 6.Ayuda                                             |")
                print("|   SALIR                                             |")
                print("|                                                     |")
                print("-------------------------------------------------------")
                print("")
                print(">> ",end="")
                opcion = input()
                opcion = opcion.strip()
                if opcion == "1":
                    os.system("cls")
                    ManejadorAFD.setEstadosUpdate(nombre)
                elif opcion == "2":
                    os.system("cls")
                    ManejadorAFD.setAlfabeto(nombre)
                elif opcion =="3":
                    os.system("cls")
                    ManejadorAFD.setEstadoInicialAFD(nombre)
                elif opcion == "4":
                    os.system("cls")
                    ManejadorAFD.setEstadoAceptacionAFD(nombre)
                elif opcion == "5":
                    os.system("cls")
                    menuTransicion(nombre)
                elif opcion == "6":
                    os.system("cls")
                    ManejadorAFD.helpCaratula()
                    ManejadorAFD.help()
                elif opcion == "ver":
                    os.system("cls")
                    ManejadorAFD.getAFD(nombre)
                elif opcion.lower() == "salir":
                    os.system("cls")
                    break
                else:
                    os.system("cls")
        else:
            menuMain()
    else:
        nombre = setNombreAFD()
        nombre = nombre.strip()
        buscado = ManejadorAFD.buscarAFD(nombre)
        if buscado != None:
            while True:
                    print("---------------------Menu AFD UPDATE-------------------")
                    print("|                                                     |")
                    print("| 1.Ingresar Estados                                  |")
                    print("| 2.Ingresar Alfabeto                                 |")
                    print("| 3.Estado Inicial                                    |")
                    print("| 4.Estado Aceptacion                                 |")
                    print("| 5.Transiciones                                      |")
                    print("| 6.Ayuda                                             |")
                    print("|   SALIR                                             |")
                    print("|                                                     |")
                    print("-------------------------------------------------------")
                    print("")
                    print(">> ",end="")
                    opcion = input()
                    opcion = opcion.strip()
                    if opcion == "1":
                        os.system("cls")
                        ManejadorAFD.setEstadosUpdate(nombre)
                    elif opcion == "2":
                        os.system("cls")
                        ManejadorAFD.setAlfabeto(nombre)
                    elif opcion =="3":
                        os.system("cls")
                        ManejadorAFD.setEstadoInicialAFD(nombre)
                    elif opcion == "4":
                        os.system("cls")
                        ManejadorAFD.setEstadoAceptacionAFD(nombre)
                    elif opcion == "5":
                        os.system("cls")
                        menuTransicion(nombre)
                    elif opcion == "6":
                        os.system("cls")
                        ManejadorAFD.helpCaratula()
                        ManejadorAFD.help()
                    elif opcion == "ver":
                        os.system("cls")
                        ManejadorAFD.getAFD(nombre)
                    elif opcion.lower() == "salir":
                        os.system("cls")
                        break
                    else:
                        os.system("cls")
        else:
            menuAFD()


def menuTransicion(nombre):
    while True:
        print("-------------------Menu Transiciones-------------------")
        print("|                                                     |")
        print("| 1.Modo No.1                                         |")
        print("| 2.Modo No.2                                         |")
        print("|   SALIR                                             |")
        print("|                                                     |")
        print("-------------------------------------------------------")
        print("")
        print(">> ",end="")
        opcion = input()
        opcion = opcion.strip()
        if opcion == "1":
            os.system("cls")
            ManejadorAFD.modoUnoTrancision(nombre)
        elif opcion == "2":
            os.system("cls")
            ManejadorAFD.modoDosTrasiciones(nombre)
        elif opcion.lower()== "salir":
            os.system("cls")
            break
        else:
            os.system("cls")
