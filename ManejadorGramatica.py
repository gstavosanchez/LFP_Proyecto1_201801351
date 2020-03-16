import os
import sys
import msvcrt
import Menu
from Gramatica import *

listaGramatica = []

def alerta(mensaje):
    os.system("cls")
    print("------------------------ALERTA-------------------------")
    print("|                                                     |")
    print("| Error:                                              |")
    print("| ->>No Se Realizo La Operacion                       |") 
    print(f"| -->>{mensaje}                                    ")
    print("|                                                     |")
    print("-------------------------------------------------------")


def newGramatica(name):
    name = name.strip()
    if duplicateData(name) == False:
        newGrammar = Gramatica(name,[],[],"",[],[])
        listaGramatica.append(newGrammar)
        return True
    else:
        alerta("Datos Duplicados")
        return False 



def duplicateData(nombre):
    nombre = nombre.strip()
    for valor in listaGramatica:
        if nombre == valor.getNombre():
            return True
    return False 

def searchGrammar(name):
    name = name.strip()
    for value in listaGramatica:
        if name == value.getNombre():
            return value
    return None     


def duplicateDataInList(name,listt):
    name = name.strip()
    for data in listt:
        if name == data:
            return True
    return False

def updateNoTerminal(grammar,listNoTerminal):
    grammar.setNoTerminal(listNoTerminal)

def updateTerminal(grammar,listTerminal):
    grammar.setTerminal(listTerminal)


def setNewNoTerminal(name):
    name = name.strip()
    grammar = searchGrammar(name)
    if grammar != None:
        x = 1
        listNoTermial = []
        while True:
            print("------------------------ALERTA-------------------------")
            print(f"| Ingrese datos No.{x}                                  |")
            print("-------------------------------------------------------")
            print("")
            print(">> ",end="")
            parameter = input()
            parameter = parameter.strip()
            parameter = parameter.upper()
            if parameter.lower() != "salir":
                if duplicateDataInList(parameter,listNoTermial) == False:
                    x +=1
                    listNoTermial.append(parameter)
                    os.system("cls")
                else:
                    os.system("cls")
            else:
                os.system("cls")
                break
        os.system("cls")
        updateNoTerminal(grammar,listNoTermial)

def setNewTerminal(name):
    name = name.strip()
    grammar =searchGrammar(name)
    if grammar != None:
        x = 1
        listTerminal = []
        while True:
            print("------------------------ALERTA-------------------------")
            print(f"| Ingrese datos No.{x}                                  |")
            print("-------------------------------------------------------")
            print("")
            print(">> ",end="")
            parameter = input()
            parameter = parameter.strip()
            parameter = parameter.lower()
            if parameter.lower() != "salir":
                if duplicateDataInList(parameter,listTerminal) == False and duplicateDataInList(parameter,grammar.getNoTerminal()) == False:
                    x += 1
                    os.system("cls")
                    listTerminal.append(parameter.lower())    
            else:
                os.system("cls")
                break
        os.system("cls")
        updateTerminal(grammar,listTerminal)
            
def setNewNTInicial(name):
    name = name.strip()
    grammar = searchGrammar(name)
    



def getGrammar(name):
    name = name.strip()
    for data in listaGramatica:
        if name == data.getNombre():
            print("Name: ",data.getNombre())
            print("No Terminal: ",data.getNoTerminal())
            print("No Teminal Inicial: ",data.getInicio())
            print("Terminal: ",data.getTerminal())
            print("Producciones: ",data.getProduccion())
            print("Gramatica Transformada: ",data.getTransformada())

    