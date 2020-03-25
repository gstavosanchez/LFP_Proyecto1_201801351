from tkinter import filedialog
from tkinter import *
from io import open
import os
import os.path
import sys
import msvcrt
import ManejadorGramatica
import ManejadorAFD


def alertaError(mensaje):
    os.system("cls")
    print("------------------------ALERTA-------------------------")
    print("|                                                     |")
    print("| Error:                                              |")
    print("| ->>No Se Realizo La Operacion                       |") 
    print(f"| -->>{mensaje}                  ")
    print("|                                                     |")
    print("-------------------------------------------------------")

def getObjet(name):
    name = name.strip()
    automata = ManejadorAFD.buscarAFD(name)
    gramatica = ManejadorGramatica.searchGrammar(name)
    if automata != None:
        return ("automata",automata)
    if gramatica != None:
        return ("grammar",gramatica)
    else:
        return (None,None)

def is_empty(data_structure):
    if data_structure:
        #print("No está vacía")
        return False
    else:
        #print("Está vacía")
        return True
    
def getRutaArchivo(nombre):
    tipo,objeto = getObjet(nombre.strip())
    if objeto != None and tipo != None:
        if tipo == "automata":
            root = Tk()
            root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("AFD files","*.afd"),("all files","*.*")))
            ruta = root.filename
            if is_empty(ruta.strip()) == False:
                ruta = f"{ruta}.afd"
                root.destroy()
                return (ruta.strip())
            else:
                alertaError("No escribio ningun nombre")
                root.destroy()
                return None
        elif tipo == "grammar":
            root = Tk()
            root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("Grammar files","*.grm"),("all files","*.*")))
            ruta = root.filename
            if is_empty(ruta.strip()) == False:
                ruta = f"{ruta}.grm"
                root.destroy()
                return (ruta.strip())
            else:
                alertaError("No escribio ningun nombre")
                root.destroy()
                return None




def transformarArchivo(nombre):
    nombre = nombre.strip()
    ruta = getRutaArchivo(nombre)
    tipo,objeto = getObjet(nombre.strip())
    if ruta != None:
        if tipo == "automata":
            texto = ""
            diccionario = objeto.getTrancisiones()
            listEstadoAceptacion = objeto.getEstadosDeAceptacion()
            for key,value in diccionario.items():
                for listCadena in value:
                    cadena = listCadena.split(" ")
                    alfabeto = cadena[0]
                    estado = cadena[1]
                    if searchInListAceptacion(key,listEstadoAceptacion) == False and searchInListAceptacion(estado,listEstadoAceptacion) == False:
                        texto = f"{key},{estado},{alfabeto};false,false"
                        writeArchivo(texto,ruta)
                    elif searchInListAceptacion(key,listEstadoAceptacion) == False and searchInListAceptacion(estado,listEstadoAceptacion) == True:
                        texto = f"{key},{estado},{alfabeto};false,true"
                        writeArchivo(texto,ruta)
                    elif searchInListAceptacion(key,listEstadoAceptacion) == True and searchInListAceptacion(estado,listEstadoAceptacion) == False:
                        texto = f"{key},{estado},{alfabeto};true,false"
                        writeArchivo(texto,ruta)
                    elif searchInListAceptacion(key,listEstadoAceptacion) == True and searchInListAceptacion(estado,listEstadoAceptacion) == True:
                        texto = f"{key},{estado},{alfabeto};true,true"
                        writeArchivo(texto,ruta)
                        
        elif tipo == "grammar":
            texto = ""
            diccionario = objeto.getProduccion()
            listEstadoAceptacion = objeto.getEstadosAceptacion()
            for key,value in diccionario.items():
                for listCadena in value:
                    if listCadena != "epsilon":
                        cadena = listCadena.split(" ")
                        alfabeto = cadena[0]
                        estado = cadena[1]
                        
                        if searchInListAceptacion(estado,listEstadoAceptacion) == True and estado == "Z":
                            texto = f"{key} > {alfabeto}"
                            writeArchivo(texto,ruta)
                        elif searchInListAceptacion(estado,listEstadoAceptacion) == True and estado != "Z":
                            texto = f"{key} > epsilon"
                            writeArchivo(texto,ruta)
                        else:
                            texto = f"{key} > {alfabeto} {estado}"
                            writeArchivo(texto,ruta)
                    else:
                        texto = f"{key} > epsilon"
                        writeArchivo(texto,ruta)
        
def searchInListAceptacion(parametro,lista):
    for value in lista:
        if value == parametro:
            return True
    return False
def writeArchivo(texto,ruta):
    archivo  = open(f"{ruta}","a")
    texto = f"{texto}\n"
    archivo.writelines(texto)
    archivo.close()
    
def wirteArchivoGraphi(texto,ruta):
    writeArchivo(texto,ruta)
    comand = 'cmd / k "%s"'%(ruta)
    os.system (comand)

def getRutaGraphiz(nombre):
    tipo,objeto = getObjet(nombre.strip())
    if tipo != None and objeto != None:
        root = Tk()
        root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))
        ruta = root.filename
        texto  = ""
        if is_empty(ruta.strip()) == False:
            rutaImagen = f"{ruta}.png"
            rutaDot = f"{ruta}.dot"
            rutaCMD = f"{ruta}.cmd"
            root.destroy()
            texto = 'cd %s \n dot -Tpng "%s" -o "%s"'%(ruta,rutaDot,rutaImagen)
            generateGraphiz(nombre,rutaDot)
            wirteArchivoGraphi(texto,rutaCMD)
        else:
            alertaError("No escribio ningun nombre")
            root.destroy()
            return None
    else:
        alertaError("No encontro el afd o gramatica")
        return None
    
                


def generateGraphiz(nombre,rutaDot):
    tipo,objeto = getObjet(nombre.strip())
    if tipo != None and objeto != None:
        bloqueUno = ""
        bloqueDos = ""
        texto = ""
        if tipo == "automata":
            listaEstados = objeto.getEstado()
            listEstadoAceptacion = objeto.getEstadosDeAceptacion()
            diccionario = objeto.getTrancisiones()
            
            for est in listaEstados:
                if searchInListAceptacion(est,listEstadoAceptacion) == True:
                    bloqueUno += '%s [shape=doublecircle] \n'%(est)
                else:
                    bloqueUno += f"{est} [] \n"
            
            for key,value in diccionario.items():
                for listCadena in value:
                    cadena = listCadena.split(" ")
                    alfabeto = cadena[0]
                    estado = cadena[1]
                    
                    bloqueDos += '%s -> %s [label="%s"] \n'%(key,estado,alfabeto)

            texto = 'digraph G { \n \n {\n  %s \n  } \n  %s \n  }'%(bloqueUno,bloqueDos)
            writeArchivo(texto,rutaDot)
            
        elif tipo == "grammar":
            pass
        
 