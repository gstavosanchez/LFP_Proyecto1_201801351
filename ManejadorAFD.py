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
    print("| Carnet:*******1                                     |")
    print("|                                                     |")
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
        nuevoAFD = AFD(nombre,[],[],"",[],{})
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

def alertaPedirDatos():
    print("------------------------ALERTA-------------------------")
    print("| Ingrese datos:                                      |")
    print("-------------------------------------------------------")

def setEstadosUpdate(nombre):
    nombre = nombre.strip()
    automata = buscarAFD(nombre)
    x = 1
    if automata != None:
        listaEstado = []
        while True:
            print("------------------------ALERTA-------------------------")
            print(f"| Ingrese datos No.{x}                                  |")
            print("-------------------------------------------------------")
            print("")
            print(">> ",end="")
            estado = input()
            estado = estado.upper() 
            estado = estado.strip()
            if estado.lower() != "salir":
                if datosDuplicadosEstadosAlfabeto(estado,listaEstado) == False:
                    x += 1
                    listaEstado.append(estado.upper())
                    os.system("cls")
                else:
                    os.system("cls")
            else:
                os.system("cls")
                break 
        os.system("cls")
        updateEstados(automata,listaEstado)



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

def updateEstdoInicial(automata,parametro):
    automata.setEstadoInicial(parametro)

def updateEstadosAceptacion(automata,listaEstadoAceptacion):
    automata.setEstadosDeAceptacion(listaEstadoAceptacion)

def updateTranciones(automata,listaTransiciones):
    automata.setTrancisiones(listaTransiciones)

def setAlfabeto(nombre):
    nombre = nombre.strip()
    automata = buscarAFD(nombre)
    listaAlfabeto = []
    x = 1
    if automata != None:
        while True:
            print("------------------------ALERTA-------------------------")
            print(f"| Ingrese datos No.{x}                                  |")
            print("-------------------------------------------------------")
            print("")
            print(">> ",end="")
            alfa = input()
            alfa = alfa.strip()
            alfa = alfa.lower()
            if alfa.lower() != "salir" and alfa.strip() != None:
                if datosDublicadosAlafabeto(alfa,listaAlfabeto) == False and datosDuplicadosEstadosAlfabeto(alfa,automata.getEstado()) == False:
                    x += 1
                    os.system("cls")
                    listaAlfabeto.append(alfa.lower())   
                else:
                    os.system("cls")
            else:
                break
        os.system("cls")
        updaAlfabeto(automata,listaAlfabeto)

        
        

def datosDublicadosAlafabeto(nombre,listaAlfabeto):
    for valor in listaAlfabeto:
        if nombre  == valor:
            return True
    return False
def datosDuplicadosEstadosAlfabeto(parametro,lista):
    for valor in lista:
        if parametro == valor:
            return True
    return False


def isInteger(val):
    try:
        isinstance(int(val), int)
        return True
    except ValueError as error:
        return False



def setEstadoInicialAFD(nombre):
    nombre = nombre.strip()
    alertaPedirDatos()
    print("")
    print(">> ",end="")
    inicial = input()
    inicial = inicial.strip()
    automata = buscarAFD(nombre)
    if automata != None:
        if datosDuplicadosEstadosAlfabeto(inicial,automata.getEstado()) == True:
            updateEstdoInicial(automata,inicial.upper())
            os.system("cls")
        else:
            alerta("No se encontro el estado")

    
def setEstadoAceptacionAFD(nombre):
    nombre = nombre.strip()
    estadosAceptacion = []
    automata =  buscarAFD(nombre)
    x = 1
    if automata != None:
        while True:
            print("------------------------ALERTA-------------------------")
            print(f"| Ingrese datos No.{x}                                  |")
            print("-------------------------------------------------------")
            print("")
            print(">> ",end="")
            aceptacion = input()
            aceptacion = aceptacion.strip()
            aceptacion = aceptacion.upper()
            if aceptacion.lower() != "salir" and aceptacion != None:
                if datosDuplicadosEstadosAlfabeto(aceptacion,automata.getEstado()) == True:
                    x += 1
                    os.system("cls")
                    estadosAceptacion.append(aceptacion.upper())
                else:
                    alerta("No se encontro el estado")
            else:
                break
        os.system("cls")
        updateEstadosAceptacion(automata,estadosAceptacion)


def getAFD(nombre):
    nombre = nombre.strip()
    for valor in listaAFD:
        if nombre == valor.getNombre():
            print(valor.getNombre())
            print(valor.getEstado())
            print(valor.getAlfabeto())
            print(valor.getEstadoInicial())
            print(valor.getEstadosDeAceptacion())
            print(valor.getTrancisiones())


def modoUnoTrancision(nombre):
    nombre = nombre.strip()
    automata  = buscarAFD(nombre)
    x = 1
    listaTrancision = {}
    if automata != None:
        while True:
            print("------------------------ALERTA-------------------------")
            print(f"| Ingrese datos No.{x}                                  |")
            print("-------------------------------------------------------")
            print("")
            print(">> ",end="")
            aceptacion = input()
            aceptacion = aceptacion.strip()
            if aceptacion != "salir":
                key,value = analizadorTrancision(automata,aceptacion)
                if key != None and value != None:
                    #if analizadoAFN(automata,key,aceptacion) == False: 
                    listaTrancision[key] = value
                    x +=1
                    updateTranciones(automata,listaTrancision)
                    os.system("cls")       
            else:
                break
        os.system("cls")
        #updateTranciones(automata,listaTrancision)

def analizadorTrancision(automata,cadena):
    try:
        ca = cadena
        pos = cadena.split(";")
        estados = pos[0]
        alfabeto = pos[1]
        estados = estados.split(",")
        for valor in estados:
            if valor != "-":
                if datosDuplicadosEstadosAlfabeto(valor,automata.getEstado()) == False:
                    alerta("No existe el Estado")
                    return None,None
        for parametro in alfabeto:
            if datosDublicadosAlafabeto(parametro,automata.getAlfabeto()) == False:
                alerta("No existe el Alfabeto o Terminal")
                return None,None
        listaTransicion = getListDiccionario(automata,estados[0])
        if listaTransicion == None:
            listaTransicion = []
            estdoDos = estados[1]
            parametro = f"{alfabeto} {estdoDos}"
            listaTransicion.append(parametro)
            return(estados[0],listaTransicion)
        else:
            if analizadoAFN(automata,estados[0],ca) == False:
                estdoDos = estados[1]
                parametro = f"{alfabeto} {estdoDos}"
                listaTransicion.append(parametro)
                return(estados[0],listaTransicion)
            else:
                return(None,None)
    except IndexError as e:
        alerta(e)
        return None,None
        

def getListDiccionario(automata,clave):
    diccionario = automata.getTrancisiones()
    for key,value in diccionario.items():
        if clave == key:
            return value
    return None


def analizadoAFN(automata,clave,valor):
    try:
        valor = valor.split(";")
        lista = getListDiccionario(automata,clave)
        if lista != None:
            for value in lista:
                value = value.split(" ")
                print(value[0])
                if valor[1] == value[0]:
                    alerta("Solo es posible con el AFN")
                    return True
            return False
        else:
            return False
    except IndexError as e:
        alerta(e)
        return True

def analizadorSimbolos(lista,cadena):
    pos = cadena.split(";")
    estados = pos[0]
    alfabeto = pos[1]
    estados = estados.split(",")
    primerEstado = estados[0]
    for valor in lista:
        primerSplit = valor.split(";")
        estadosLista = primerSplit[0]
        estadosLista = estadosLista.split(",")
        alfabetoLista = primerSplit[1]
        estadoUno = estadosLista[0]
        if primerEstado == estadoUno and alfabeto == alfabetoLista:
            alerta("Solo es posible con el AFN")
            return True
    return False
         

def modoDosTrasiciones(nombre):
    x = 3
    nombre = nombre.strip()
    automata = buscarAFD(nombre)
    #listaTransicion = []
    fila = ""
    columna = ""
    simbolos = ""
    if automata != None:
        for i in range(x):
            if i == 0:
                print("------------------------ALERTA-------------------------")
                print(f"| Ingrese Terminales o Alfabeto                      |")
                print("-------------------------------------------------------")
                print("")
                print(">> ",end="")
                aceptacion = input()
                aceptacion = aceptacion.strip()
                if analizadorAlfabetoModoDos(aceptacion,"alfabeto",automata)== True:
                    #listaTransicion.append(aceptacion)
                    fila = aceptacion
                else :
                    alerta("Intente otra vez")
                    break
            elif i == 1:
                print("------------------------ALERTA-------------------------")
                print(f"| Ingrese No Terminales o Estados                    |")
                print("-------------------------------------------------------")
                print("")
                print(">> ",end="")
                aceptacion = input()
                aceptacion = aceptacion.strip()
                if analizadorAlfabetoModoDos(aceptacion,"estado",automata) == True:
                    #listaTransicion.append(aceptacion)
                    columna = aceptacion
                else:
                    break
            elif i == 2:
                print("------------------------ALERTA-------------------------")
                print(f"| Ingrese Simbolos Destino                           |")
                print("-------------------------------------------------------")
                print("")
                print(">> ",end="")
                aceptacion = input()
                aceptacion = aceptacion.strip()
                if analizadorEstadoDestino(aceptacion,automata) == True:
                    #listaTransicion.append(aceptacion)
                    #updateTranciones(automata,listaTransicion)
                    os.system("cls")
                    simbolos = aceptacion
                    if transformarLista(fila,columna,simbolos,automata) == True:
                        os.system("cls")
                    else:
                        break
                else:
                    break
        
           
def analizadorAlfabetoModoDos(cadena,tipo,automata):
    try:
        cadena = cadena.replace("[","")
        cadena = cadena.replace("]","")
        cadena = cadena.strip()
        cadena = cadena.split(",")
        if tipo.lower() == "alfabeto":
            for valor in cadena:
                if datosDublicadosAlafabeto(valor,automata.getAlfabeto()) == False:
                    alerta("No existe el Alfabeto o Terminal")
                    return False
            return True
        if tipo.lower() == "estado":
            for valor in cadena:
                if datosDuplicadosEstadosAlfabeto(valor,automata.getEstado()) == False:
                    alerta("No existe el Estado")
                    return False
            return True
    except IndexError as e:
        alerta(e)
        return False
   
def analizadorEstadoDestino(cadena,automata):
    try:
        cadena = cadena.replace("[","")
        cadena = cadena.replace("]","")
        cadena = cadena.split(";")
        for valor in cadena:
            valor = valor.split(",")
            for parametro in valor:
                if parametro != "-":
                    if datosDuplicadosEstadosAlfabeto(parametro,automata.getEstado()) == False:
                        alerta("No existe el Estado")
                        return False
        return True
    except IndexError as e:
        return False


def transformarLista(listaColumnas,listaFilas,listaSimbolos,automata):
    try:
        diccionario = {}
        listaColumnas = listaColumnas.replace("[","")
        listaColumnas = listaColumnas.replace("]","")

        listaFilas = listaFilas.replace("[","")
        listaFilas = listaFilas.replace("]","")

        listaSimbolos = listaSimbolos.replace("[","")
        listaSimbolos = listaSimbolos.replace("]","")

        listaColumnas = listaColumnas.split(",")
        listaFilas = listaFilas.split(",")
        listaSimbolos = listaSimbolos.split(";")
        
        for i in range(len(listaSimbolos)):
            #print("-----------------------------------------------------------------")
            #print("Simbolos:",listaSimbolos[i]," Filas:",listaFilas[i])
            lista = listaSimbolos[i]
            lista = lista.split(",")
            for x in range(len(lista)):
                #print("Filas:",listaFilas[i]," Simbolos:",lista[x]," Columnas:",listaColumnas[x])
                #print("De:",listaFilas[i]," con:",listaColumnas[x]," Hacia:",lista[x])
                de = listaFilas[i]
                con = listaColumnas[x]
                hacia = lista[x]
                cadena = f"{de},{hacia};{con}"
                #print(cadena)
                keys,valores = analizadorTrancision(automata,cadena)
                if keys != None and valores != None:
                    diccionario[keys] = valores
                    updateTranciones(automata,diccionario)
                else:
                    return False
        return True    
    except IndexError as e:
        alerta(e)
        return False