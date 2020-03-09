import os
import sys
import msvcrt
import Menu
def caratula():
    os.system("cls")
    print("-------------------------1S2020------------------------")
    print("|                                                     |")
    print("| Universidad De San Carlos De Guatemala              |")
    print("| Lenguales Formales de Programacion                  |")
    print("| Seccion B-                                          |")
    print("|                                                     |")
    print("| Elmer Gustavo Sanchez Garcia                        |")
    print("| 201801351                                           |")
    print("-------------------------------------------------------")


def pushButton():
    while True:
        m = str(msvcrt.getch(),'utf -8')
        if m == "\r":
            os.system("cls")
            Menu.menuMain()
            break
        else:
            os.system("cls")
            print("Presione Enter para continuar")
            print("")
            caratula()

caratula()
pushButton()