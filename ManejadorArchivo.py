from tkinter import filedialog
from tkinter import *
from io import open
import os
import sys
import msvcrt
import ManejadorAFD
import ManejadorGramatica


def alertaError(mensaje):
    os.system("cls")
    print("------------------------ALERTA-------------------------")
    print("|                                                     |")
    print("| Error:                                              |")
    print("| ->>No Se Realizo La Operacion                       |") 
    print(f"| -->>{mensaje}                  ")
    print("|                                                     |")
    print("-------------------------------------------------------")

def getRuta():
    try:
        root = Tk()
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("AFD files","*.afd"),("all files","*.*")))
        #print (root.filename)
        ruta = root.filename
        name = os.path.split(ruta)
        name = name[1]
        name = name.split(".")
        if is_empty(ruta) == False :
            if name[1] == "afd":
                #print("Nombre Archivo:",name[0]," Tipo:",name[1])
                nombreAFD = name[0]
                nombreAFD = nombreAFD.strip()
                if ManejadorAFD.newAFD(nombreAFD) == True:
                    #Button(root, text="Quit", command=root.destroy).pack()
                    #root.mainloop()
                    root.destroy()
                    return ruta,nombreAFD
                else:
                    return None
            else:
                getRuta()
        else:
            alertaError("No selecciono ningun archivo")
    except IndexError as e:
        alertaError(e)
    
def readArchivo():
    try:
        ruta,automata = getRuta()
        if ruta != None or is_empty(ruta) == False:
            archivo = open(f"{ruta}","r")
            texto = archivo.readlines()
            #print(texto)
            analizadorAfd(texto,automata)
    except (FileNotFoundError, IOError):
        alertaError("Error en la lectua")
    
def analizadorAfd(arreglo,automata):
    for i,value in enumerate(arreglo):
        newTerminal(value,automata)


def newTerminal(cadena,nombre):
    automata = ManejadorAFD.buscarAFD(nombre.strip())
    cadena = cadena.strip()
    newCadena = cadena
    if automata != None:
        listaEstados = automata.getEstado()
        listaEstadosAceptacion = automata.getEstadosDeAceptacion()
        listaAlfabeto = automata.getAlfabeto()
        estadoInicial = automata.getEstadoInicial()
        cadena = cadena.split(";")
        parteUno = cadena[0]
        parteUno = parteUno.split(",")
        parteDos = cadena[1]
        parteDos = parteDos.split(",")
        for i in range(len(parteUno)):
            for x in range(len(parteDos)):
                if i == 0:
                    if is_empty(estadoInicial) == True:
                        estadoInicial = parteUno[i] 
                        ManejadorAFD.updateEstdoInicial(automata,estadoInicial)
                if i == x:
                    #print("Estado: ",parteUno[x])
                    if ManejadorAFD.datosDuplicadosEstadosAlfabeto(parteUno[x],listaEstados) == False:
                        listaEstados.append(parteUno[x])
                    if parteDos[x].lower() == "true":
                        if ManejadorAFD.datosDuplicadosEstadosAlfabeto(parteUno[x],listaEstados) == True and ManejadorAFD.datosDuplicadosEstadosAlfabeto(parteUno[x],listaEstadosAceptacion) == False:
                            #print("Estado de Aceptacion:",parteUno[x]," Condicion",parteDos[x])
                            listaEstadosAceptacion.append(parteUno[x])
                elif i == len(parteUno) - 1:
                    if ManejadorAFD.datosDuplicadosEstadosAlfabeto(parteUno[i],listaAlfabeto) == False:
                        #print("Alfabeto",parteUno[i])
                        listaAlfabeto.append(parteUno[i])
        #print(listaEstados)
        ManejadorAFD.updateEstados(automata,listaEstados)
        #print(listaEstadosAceptacion)
        ManejadorAFD.updateEstadosAceptacion(automata,listaEstadosAceptacion)
        #print(listaAlfabeto)
        ManejadorAFD.updaAlfabeto(automata,listaAlfabeto)
        transformarAgregarTranciones(cadena[0],automata)

def transformarAgregarTranciones(cadena,automata):
    cadena = cadena.split(",")
    de = cadena[0]
    hacia = cadena[1]
    con = cadena[2]
    texto = f"{de},{hacia};{con}"
    #print(texto)
    diccionario = automata.getTrancisiones()
    key,value = ManejadorAFD.analizadorTrancision(automata,texto)
    if key != None and value != None:
        diccionario[key] = value
        ManejadorAFD.updateTranciones(automata,diccionario)
        os.system("cls")
    else:
        alertaError("No se gurardo la Trancision")
    
       
        



def is_empty(data_structure):
    if data_structure:
        #print("No está vacía")
        return False
    else:
        #print("Está vacía")
        return True
    