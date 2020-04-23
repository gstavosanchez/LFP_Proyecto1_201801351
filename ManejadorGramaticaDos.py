import os
import sys
import msvcrt
import Menu
from GramaticaDos import *

listaGramaticaDos = []

def alerta(mensaje):
    os.system("cls")
    print("------------------------ALERTA-------------------------")
    print("|                                                     |")
    print("| Error:                                              |")
    print("| ->>No Se Realizo La Operacion                       |") 
    print(f"| -->>{mensaje}             ")
    print("|                                                     |")
    print("-------------------------------------------------------")

def duplicateData(name):
    name = name.strip()
    for valor in listaGramaticaDos:
        if valor.getNombre() == name:
            return True
    return False

def getGramaticaDos(name):
    name = name.strip()
    for valor in listaGramaticaDos:
        if valor.getNombre() == name:
            return valor
    return None

def getObjeto(nombre):
    nombre = nombre.strip()
    for valor in listaGramaticaDos:
        if valor.getNombre() == nombre:
            return valor
    return None


def newGramaticaDos(name):
    name = name.strip()
    if duplicateData(name) == False:
        nuevaGramtica = GramaticaDos(name,[],[],"",{},{})
        listaGramaticaDos.append(nuevaGramtica)
        return True
    else:
        alerta("Datos Duplicados")
        return False

def verGramatica(name):
    name = name.strip()
    for gramatica in listaGramaticaDos:
        if name == gramatica.getNombre():
            print(f" Nombre: ",gramatica.getNombre())
            print(f" Terminal: ",gramatica.getTerminal())
            print(f" No Terminal: ",gramatica.getNoTerminal())
            print(f" No Ter. Incial: ",gramatica.getNoTerminalInicial())
            print(f" Produccion: ",gramatica.getProduccion())
        
        

def updateTerminal(grammarDos,listaTerminal):
    grammarDos.setTerminal(listaTerminal)
    
def updateNoTerminal(grammarDos,listaNoTerminal):
    grammarDos.setNoTerminal(listaNoTerminal)

def updateNoTerminalIncial(grammarDos,parametro):
    grammarDos.setNoTerminalIncial(parametro)

def updateProduccion(grammarDos,parametro):
    grammarDos.setProduccion(parametro)

def updateProTransformada(grammarDos,parametro):
    grammarDos.setProTransformada(parametro)



def datosDuplicadosAnyList(name,lista):
    for valor in lista:
        if name == valor:
            return True
    return False

def setNewTerminal(nombre):
    nombre = nombre.strip()
    gramatica = getObjeto(nombre)
    if gramatica != None:
        x = 1
        listaTemp = []
        while True:
            print("--------------------Nueva Terminal---------------------")
            print(f"| Ingrese datos No.{x}                                  |")
            print("-------------------------------------------------------")
            print("")
            print(">> ",end="")
            dato = input()
            dato = dato.strip()
            dato = dato.lower()
            if dato.lower() != "salir":
                if datosDuplicadosAnyList(dato,listaTemp) == False:
                    listaTemp.append(dato)
                    os.system("cls")
                    x += 1
                else:
                    os.system("cls")
                    alerta("Ya existe el terminal: "+dato)     
            else:
                os.system("cls")
                break
        os.system("cls")
        updateTerminal(gramatica,listaTemp)
                
    else:
        os.system("cls")
        alerta("No se puede realizar la operacion")



        
def setNewNoTerminal(nombre):
    nombre = nombre.strip()
    gramatica = getObjeto(nombre)
    if gramatica != None:
        x = 1
        listaTemp = []
        while True:
            print("------------------Nueva No Terminal--------------------")
            print(f"| Ingrese datos No.{x}                                  |")
            print("-------------------------------------------------------")
            print("")
            print(">> ",end="")
            dato = input()
            dato = dato.strip()
            dato = dato.upper()
            if dato.upper() != "SALIR":
                if datosDuplicadosAnyList(dato,listaTemp) == False:    
                    listaTemp.append(dato)
                    os.system("cls")
                    x += 1
                else:
                    os.system("cls")
                    alerta("Ya existe el no terminal: "+dato)  
            else:
                os.system("cls")
                break
        os.system("cls")
        updateNoTerminal(gramatica,listaTemp)
                
    else:
        os.system("cls")
        alerta("No se puede realizar la operacion")



def setNTInicial(nombre):
    nombre = nombre.strip()
    gramatica = getObjeto(nombre)
    if gramatica != None:
        while True:
            print("------------------------Nuevo--------------------------")
            print("| Ingrese No Terminal Inicial:                         |")
            print("-------------------------------------------------------")
            print("")
            print(">> ",end="")
            dato = input()
            dato = dato.strip()
            dato = dato.upper()
            if dato.upper() != "SALIR":
                if datosDuplicadosAnyList(dato,gramatica.getNoTerminal()) == True:
                    updateNoTerminalIncial(gramatica,dato)
                    os.system("cls")
                    break
                else:
                   alerta("No existe el no terminal: "+dato+" en la lista")   
            else:
                os.system("cls")
                break


def setProduccion(nombre):
    nombre = nombre.strip()
    gramatica = getObjeto(nombre)
    if gramatica != None:
        diccionarioTemp = {}
        x = 1
        recurividadad = False
        while True:
            print("------------------Nueva Produccion--------------------")
            print(f"| Ingrese Produccion No.{x}                           |")
            print("------------------------------------------------------")
            print("")
            print(">> ",end="")
            dato = input()
            dato = dato.strip()
            if dato.lower() != "salir":
                key,valor,recursivo = analisis(gramatica,dato)
                if key != None and valor != None and recursivo != None:     
                    diccionarioTemp[key] = valor
                    recurividadad = recursivo
                    updateProduccion(gramatica,diccionarioTemp)
                    os.system("cls")
                    x +=1
            else:
                os.system("cls")
                break
        updateProduccion(gramatica,diccionarioTemp)
            
def analisis(gramantica,cadena):
    try:
        cadena = cadena.strip()
        cadena = cadena.split(">")
        clave = cadena[0].strip()
        listaPro = cadena[1].strip()
        recursivo = es_recursivo(gramantica,listaPro)
        if datosDuplicadosAnyList(clave,gramantica.getNoTerminal()) == True and exist(gramantica,listaPro) == True:
            listaTemp = getListaInDiccionario(gramantica,clave)
            if listaTemp == None:
                listaTemp = []
                listaTemp.append(listaPro)
                return(clave,listaTemp,recursivo)
            else:
                listaTemp.append(listaPro)
                return(clave,listaTemp,recursivo)
        else:
            alerta("No se encontro el Terminal o No Terminal :(")
            return(None,None,None)
            
        
        
    except IndexError as e:
        alerta(e)
        return(None,None,None)
        
      
# Retornar la lista de cierta clave
def getListaInDiccionario(grammar,clave):
    diccionario = grammar.getProduccion()
    for key,value in diccionario.items():
        if clave == key:
            return value
    return None

## Verificar si existe esta cadena BmnZ
def exist(gramatica,cadena):
    if cadena != "epsilon":
        for i in range(len(cadena)):
            if es_numero(cadena[i]) == False:
                if es_mayuscula(cadena[i]) == True:
                    if datosDuplicadosAnyList(cadena[i],gramatica.getNoTerminal()) == False:
                        #print("No esta:",cadena[i])
                        return False
                else:
                    if datosDuplicadosAnyList(cadena[i],gramatica.getTerminal()) == False:
                        #print("No esta:",cadena[i])
                        return False
            else:
                if datosDuplicadosAnyList(cadena[i],gramatica.getTerminal()) == False:
                    #print("No esta:",cadena[i])
                    return False
        return True
    else:
        return False
    
# Verificar si es recursiva
def es_recursivo(gramatica,cadena):
    if cadena != "epsilon":
        if len(cadena) > 1:
            for i in range(len(cadena)):
                #print("Numero:",i," Letra:",cadena[i])
                if i == 0:
                    if datosDuplicadosAnyList(cadena[i],gramatica.getNoTerminal()) == True:
                        return True
            return False
        else:
            return False
        
            


def es_mayuscula(letra):
    if letra == letra.upper():
        return True
    elif letra == letra.lower():
        return False

def es_numero(parametro):
    return (parametro.isnumeric())



def borrar_cadena(nombre):
    nombre = nombre.strip()
    gramatica = getObjeto(nombre)
    if gramatica != None:
        x = 1
        while True:
            print("------------------Borrar Produccion--------------------")
            print(f"| Ingrese dato a ELIMINAR No.{x}                        |")
            print("-------------------------------------------------------")
            print("")
            print(">> ",end="")
            dato = input()
            dato = dato.strip()
            if dato != "salir":
                if analizar_borrador(gramatica,dato) == True:
                    x += 1
                    os.system("cls")
            else:
                os.system("cls")
                break  
            
    else:
        os.system("cls")
        alerta("No se puede realizar la operacion")


def analizar_borrador(gramatica,cadena):
    try:
        aux = cadena.strip()
        cadena = cadena.strip()
        cadena = cadena.split(">")
        clave = cadena[0].strip()
        listado = cadena[1].strip()
        diccionario = gramatica.getProduccion()
        if datosDuplicadosAnyList(clave,gramatica.getNoTerminal()) == True and exist(gramatica,listado) == True:
            listaTemp = getListaInDiccionario(gramatica,clave)
            if listaTemp != None:
                if datosDuplicadosAnyList(listado,listaTemp) == True:
                    listaTemp.remove(listado)
                    diccionario[clave] = listaTemp
                    updateProduccion(gramatica,diccionario)
                    return True
                else:
                    alerta("Revise sus Parametros")
                    return False   
            else:
                alerta("Esta vacio sus producciones.")
                return False
        else:
            alerta("No se encontro el Terminal o no Terminal ):")
            return False
    except IndexError as e:
        alerta(e)
        return False


def tranformar_gramtica(gramatica):
    pass
