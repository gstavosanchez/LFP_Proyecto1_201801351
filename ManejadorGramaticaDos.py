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
            print(f" Produccion Trans: ",gramatica.getProTransformada())
        
        

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
    name = name.strip()
    for valor in lista:
        if valor == name:
            return True
    return False
    
def datos_Duplicados_Any(name,lista):
    name = name.strip()
    #print(name)
    if es_numero(name) == False:
        if es_mayuscula(name) == True:
            for valor in lista:
                if valor == name:
                    #print("Valor:",valor)
                    if es_mayuscula(valor) == True and es_mayuscula(name) == True:
                        return True
            return False
        elif es_mayuscula(name) == False:
            for valor in lista:
                if valor == name:
                    #print("Valor:",valor)
                    if es_mayuscula(valor) == False and es_mayuscula(name) == False:
                        return True
            return False
    else:
        for valor in lista:
            if valor == name:
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
        if recursivo_mejorado(gramatica) == True:
            tranformar_gramtica(gramatica)    
        
            
def analisis(gramantica,cadena):
    try:
        cadena = cadena.strip()
        cadena = cadena.split(">")
        clave = cadena[0].strip()
        listaPro = cadena[1].strip()
        recursivo = False
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
        
      
# Retornar la lista de cierta clave de un diccionario
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
        for i in range(len(cadena)):
            if i == 0:
                #print("Metodo Recursivo: " +cadena[i])
                if datos_Duplicados_Any(cadena[i],gramatica.getNoTerminal()) == True:
                    return True
        return False
    else:
        return False

def recursivo_mejorado(gramatica):
    diccionario = gramatica.getProduccion()
    inicio = gramatica.getNoTerminalInicial()
    if inicio != None and size_diccionario(gramatica):
        for key,value in diccionario.items():
            listaKey = value
            for cadena in listaKey:
                # print(len(cadena))
                # print("Key:",key)
                # print("Incio",inicio)
                if key == inicio and len(cadena) == 1 and datos_Duplicados_Any(cadena,gramatica.getNoTerminal()) == True:
                    print("")
                else:
                    if es_recursivo(gramatica,cadena) == True:
                        return True             
        return False
    else:
        alerta("Falta datos para determinar recursividad :(")
        return False
        


def get_letraRecursiva(gramatica,cadena):
    if cadena != "epsilon":
        for i in range(len(cadena)):
            #print("Numero:",i," Letra:",cadena[i])
            if i == 0:
                if datosDuplicadosAnyList(cadena[i],gramatica.getNoTerminal()) == True:
                    return cadena[i]
        return None
    else:
        return None
        
            


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


# Retornar el tamaño del diccionario
def size_diccionario(grammar):
    diccionario = grammar.getProduccion()
    x = 0
    for key,value in diccionario.items():
        x +=1
    return x


def tranformar_gramtica(gramatica):
    if size_diccionario(gramatica) != 0:
        eps = "epsilon"
        diccionario = gramatica.getProduccion()
        dicc_aux = {}
        for  key,value in diccionario.items():
            listaKey = value
            for cadena in listaKey:
                #print("Clave: ",key+" Valor:",cadena)
                if len(cadena) ==  1 and datosDuplicadosAnyList(cadena,gramatica.getNoTerminal()) == True:
                    listaAux = []
                    listaAux.append(cadena)
                    dicc_aux[key] = listaAux
                else:
                    #Agregar los nuevos NO Terminales AP,ZP
                    no_terminal = key+"P"
                    if es_recursivo(gramatica,cadena) == True:
                        if datosDuplicadosAnyList(no_terminal,gramatica.getNoTerminal()) == False:
                            listaTerminal = gramatica.getTerminal()
                            listaNoTerminal = gramatica.getNoTerminal()
                            listaNoTerminal.append(no_terminal)
                            updateNoTerminal(gramatica,listaNoTerminal)
                            # Generar la nueva cadena mnZ Ap
                            letra = get_letraRecursiva(gramatica,cadena)
                            cadenaNueva = cadena.replace(letra,"",1)
                            cadenaNueva = cadenaNueva+" "+no_terminal
                            cadenaNueva = no_terminal+">"+cadenaNueva
                            cadenaEps = no_terminal+">"+eps
                            #print(cadenaNueva)
                            #print(cadenaEps)
                            #Agregar al diccionario
                            cla,val = analisis_transformada(gramatica,cadenaNueva)
                            if cla != None and val != None:
                                listaTerminal.append(eps)
                                dicc_aux[cla] = val
                                updateProTransformada(gramatica,dicc_aux)
                                updateTerminal(gramatica,listaTerminal)
                            cl,va = analisis_transformada(gramatica,cadenaEps)
                            if cl != None and va != None:
                                dicc_aux[cl]= va
                                updateProTransformada(gramatica,dicc_aux)
                    else:
                        # Generar las nuevas cadenas A> xC AP
                        cadenaNuevaDos = cadena+" "+no_terminal
                        cadenaNuevaDos = key+">"+cadenaNuevaDos
                        #print(cadenaNuevaDos)
                        cla,val = analisis_transformada(gramatica,cadenaNuevaDos)
                        if cla != None and val != None:
                            dicc_aux[cla] = val
                            updateProTransformada(gramatica,dicc_aux)
                
    else:
        alerta("Sus producciones estan vacias")


def analisis_transformada(gramantica,cadena):
    try:
        cadena = cadena.split(">")
        clave = cadena[0].strip()
        listaPro = cadena[1]
        if listaPro.lower() != "epsilon":
            if datosDuplicadosAnyList(clave,gramantica.getNoTerminal()) == True:
                listaTemp = get_lista_Transformada(gramantica,clave)
                if listaTemp == None:
                    listaTemp = []
                    listaTemp.append(listaPro)
                    return(clave,listaTemp)
                else:
                    listaTemp.append(listaPro)
                    return(clave,listaTemp)
            else:
                alerta("No se encontro el Terminal o No Terminal :(")
                return(None,None,None)
        else:
            if datosDuplicadosAnyList(clave,gramantica.getNoTerminal()) == True:
                listaTemp = get_lista_Transformada(gramantica,clave)
                if listaTemp == None:
                    listaTemp = []
                    listaTemp.append(listaPro)
                    return(clave,listaTemp)
                else:
                    listaTemp.append(listaPro)
                    return(clave,listaTemp)
            else:
                alerta("No se encontro el Terminal o No Terminal :(")
                return(None,None,None)
    except IndexError as e:
        alerta(e)
        return(None,None,None)
        
      
# Retornar la lista de cierta clave de un diccionario de la transformada
def get_lista_Transformada(grammar,clave):
    diccionario = grammar.getProTransformada()
    for key,value in diccionario.items():
        if clave == key:
            return value
    return None
