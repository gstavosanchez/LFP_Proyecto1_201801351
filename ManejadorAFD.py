import os
import sys
import msvcrt
import Menu
from AFD import *

listaAFD = []

def helpCaratula():
    os.system("cls")
    print("-------------------------1S2020------------------------")
    print("|                                                     |")
    print("| Lenguales Formales de Programacion                  |")
    print("| Seccion B                                           |")
    print("| Ing.Zulma                                           |")
    print("| Aux: Luis Javier Yela                               |")
    print("| Carnet:                                             |")
    print("-------------------------------------------------------")

def help():
    while True:
        m = str(msvcrt.getch(),'utf -8')
        if m == "\r":
            os.system("cls")
            Menu.menuAFD()
            break
        else:
            helpCaratula()

def newAFD(nombre):
    nombre = nombre.strip()
    if datosDuplicados(nombre) == False:
        nuevoAFD = AFD(nombre,[],[],"",[],[])
        listaAFD.append(nuevoAFD)
        return True
    else:
        alerta("Datos Duplicados")
        return False

def buscarAFD(nombre):
    nombre = nombre.strip()
    for valor in listaAFD:
        if nombre == valor.getNombre():
            return valor

def datosDuplicados(nombre):
    nombre = nombre.strip()
    for valor in listaAFD:
        if nombre == valor.getNombre():
            return True
    return False        

def alerta(mensaje):
    os.system("cls")
    print("------------------------ALERTA-------------------------")
    print("|                                                     |")
    print("| Error:                                              |")
    print("| ->>No Se Realizo La Operacion                       |") 
    print(f"| -->>{mensaje}                                    ")
    print("|                                                     |")
    print("-------------------------------------------------------")

def setEstados(nombre):
    nombre = nombre.strip()
    print("Numero de estados")
    print(">> ",end="")
    numero = input()
    numero = numero.strip()
    if isInteger(numero) == True:
        listaEstado = []
        automata = buscarAFD(nombre)
        numero = int(numero)
        if automata != None:
            for i in range(numero):
                print("Ingrese su estado No. ",i +1)
                print(">> ",end="")
                parametro = input()
                listaEstado.append(parametro.strip())
            os.system("cls")
            updateEstados(automata,listaEstado)           
        else:
            alerta("No se encontro el AFD")
            Menu.menuAFD()
    else:
        alerta("No es numero")
        #Menu.menuAFD()

def updateEstados(automata,listaEstados):
    automata.setEstado(listaEstados)
    
def updaAlfabeto(automata,listaAlfabeto):
    automata.setAlfabeto(listaAlfabeto)

def isInteger(val):
    try:
        isinstance(int(val), int)
        return True
    except ValueError as error:
        return False
