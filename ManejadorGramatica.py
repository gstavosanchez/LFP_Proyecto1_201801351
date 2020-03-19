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
        newGrammar = Gramatica(name,[],[],"",{},[],[])
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

def updateNTInicial(grammar,parametro):
    grammar.setInicio(parametro)

def updateProduccion(grammar,diccionario):
    grammar.setProduccion(diccionario)

def updateAceptacion(grammar,lisAceptacion):
    grammar.setEstadosAceptacion(lisAceptacion)

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
    if grammar != None:
        print("------------------------ALERTA-------------------------")
        print("| Ingrese datos:                                      |")
        print("-------------------------------------------------------")
        print("")
        print(">> ",end="")
        parameter = input()
        parameter = parameter.strip()
        if duplicateDataInList(parameter,grammar.getNoTerminal()) == True:
            updateNTInicial(grammar,parameter)
            os.system("cls")
        else:
            alerta("No se encontro el estado")

        

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
            print("Estados Aceptacion: ",data.getEstadosAceptacion())

    
def setNewProduccion(name):
    name = name.strip()
    grammar = searchGrammar(name)
    if grammar != None:
        x = 1
        diccionari = {}
        while True:
            print("------------------------ALERTA-------------------------")
            print(f"| Ingrese datos No.{x}                                  |")
            print("-------------------------------------------------------")
            print("")
            print(">> ",end="")
            parameter = input()
            parameter = parameter.strip()
            if parameter.lower() != "salir":
                key,value = setProduccionInDiccionari(parameter,grammar)
                if key != None and value != None:
                    x += 1
                    diccionari[key] = value
                    updateProduccion(grammar,diccionari)
                    os.system("cls")
            else:
                os.system("cls")
                break
        os.system("cls")
        updateProduccion(grammar,diccionari)
        setEstadoAceptacionDic(grammar,diccionari)
        



def setProduccionInDiccionari(cadena,grammar):
    try:
        cadena = cadena.split(">")
        noTerminal = cadena[0].strip().upper()
        parametro = cadena[1]
        if parametro.lower() != "epsilon":
            posDos = cadena[1].rstrip()
            posDos = posDos.split(" ")
            terminal = posDos[0]
            noTerminalAndTer = posDos[1]
            if  duplicateDataInList(noTerminal,grammar.getNoTerminal()) == True and duplicateDataInList(terminal,grammar.getTerminal()) == True and duplicateDataInList(noTerminalAndTer,grammar.getNoTerminal()) == True:
                listaProduccion = getListDiccionario(grammar,noTerminal.upper().strip())
                if listaProduccion == None:
                    listaProduccion = []
                    listaProduccion.append(parametro.rstrip())
                    return(noTerminal,listaProduccion)
                else:
                    print("Esta en el else")
                    listaProduccion.append(parametro)
                    return(noTerminal,listaProduccion)
            else:
                alerta("Error en el Terminal o No terminal")
                return None
        else:
            if  duplicateDataInList(noTerminal,grammar.getNoTerminal()) == True:
                listaProduccion = getListDiccionario(grammar,noTerminal.upper().strip())
                if listaProduccion == None:
                    listaProduccion = []
                    listaProduccion.append(parametro.rstrip())
                    return(noTerminal,listaProduccion)
                else:
                    print("Esta en el else")
                    listaProduccion.append(parametro)
                    return(noTerminal,listaProduccion)
            else:
                alerta("Error No terminal")
                return None
    except IndexError as e:
        alerta(e)
        return None


def getListDiccionario(grammar,clave):
    diccionario = grammar.getProduccion()
    for key,value in diccionario.items():
        if clave == key:
            #print(value)
            return value
        
def setEstadoAceptacionDic(grammar,diccionario):
    lista = []
    for key,value in diccionario.items():
        for valores in value:
            if valores == "epsilon":
                lista.append(key.strip())
    updateAceptacion(grammar,lista)
    
    