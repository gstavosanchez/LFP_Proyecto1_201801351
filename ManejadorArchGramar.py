from tkinter import filedialog
from tkinter import *
from io import open
import os
import sys
import msvcrt
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
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Grammar files","*.grm"),("all files","*.*")))
        ruta = root.filename
        name = os.path.split(ruta)
        name = name[1]
        name = name.split(".")
        if is_empty(ruta) == False:
            if name[1] == "grm":
                nombreGramar = name[0]
                nombreGramar = nombreGramar.strip()
                if ManejadorGramatica.newGramatica(nombreGramar) == True:
                    root.destroy()
                    return ruta,nombreGramar
                else:
                    return None,None
            else:
                getRuta()
        else:
            alertaError("No selecciono ningun archivo")
            root.destroy()
            return None,None
    except IndexError as e:
        alertaError(e)
        return None,None


def readArchivo():
    try:
        ruta,gramatica = getRuta()
        if ruta != None and gramatica != None and is_empty(ruta)== False:
            archivo = open(f"{ruta}","r")
            texto = archivo.readlines()
            analizaodrGrammar(texto,gramatica)
    except(FileNotFoundError,IOError):
        alertaError("Error en la lectura")

def analizaodrGrammar(arreglo,gramatica):
    for i,value in enumerate(arreglo):
        newGrammar(value,gramatica)

def newGrammar(cadena,nombre):
    try:
        grammar = ManejadorGramatica.searchGrammar(nombre.strip())
        cadena = cadena.strip()
        if grammar != None:
            newCadena = cadena
            listNoTerminal = grammar.getNoTerminal()
            listTerminal = grammar.getTerminal()
            inicioNT = grammar.getInicio()
            listEstadosAceptacion = grammar.getEstadosAceptacion()
            cadena = cadena.split(">")
            parteUno = cadena[0]
            parteDos = cadena[1]
            parte2 = cadena[1]
            parteUno = parteUno.strip()
            parteDos = parteDos.lstrip()
            parteDos = parteDos.split(" ")
            for i in range(len(parteDos)):
                for x in range(len(parteUno)):
                    if i == x:
                        #print("Estado:",parteUno[x]," con:",parteDos[i])
                        if ManejadorGramatica.duplicateDataInList(parteUno[x],listNoTerminal) == False:
                            listNoTerminal.append(parteUno[x])
                        if ManejadorGramatica.duplicateDataInList(parteDos[i],listTerminal) == False and parteDos[i].lower() != "epsilon":
                            listTerminal.append(parteDos[i])
                        if i == 0:
                            if is_empty(inicioNT) == True and ManejadorGramatica.duplicateDataInList(parteUno[x],listNoTerminal) == True:
                                inicioNT = parteUno[x]
                                ManejadorGramatica.updateNTInicial(grammar,inicioNT)
                        
                        if parteDos[x].lower() == "epsilon":
                            if ManejadorGramatica.duplicateDataInList(parteUno[x],listNoTerminal) == True and ManejadorGramatica.duplicateDataInList(parteUno[x],listEstadosAceptacion) == False:
                                listEstadosAceptacion.append(parteUno[x])                             
                                
                    else:
                        #print("Estado:",parteDos[i])
                        if ManejadorGramatica.duplicateDataInList(parteDos[i],listNoTerminal) == False:
                            listNoTerminal.append(parteDos[i])   
                            #print("Letra:",parteDos[i]," Pos:",i)
            
            
            if len(parteDos) - 1  == 0:
                if parte2.strip() != "epsilon":
                    if ManejadorGramatica.duplicateDataInList("Z",listNoTerminal) == False and ManejadorGramatica.duplicateDataInList("Z",listEstadosAceptacion) == False:
                        listNoTerminal.append("Z")
                        listEstadosAceptacion.append("Z")           
                                  
            #print("No terminal:",listNoTerminal)
            ManejadorGramatica.updateNoTerminal(grammar,listNoTerminal)
            #print("Terminal:", listTerminal)
            ManejadorGramatica.updateTerminal(grammar,listTerminal)
            ManejadorGramatica.updateAceptacion(grammar,listEstadosAceptacion)
            #print("NT Inicio:",inicioNT)
            newProduccion(grammar,newCadena)
            

            
    except IndexError as e:
        alertaError(e)
    
def duplicateCadena():
    pass

def newProduccion(grammar,cadena):
    texto = ""
    diccionario = grammar.getProduccion()
    if len(cadena)-1 == 4:
        cadena = cadena.split(">")
        if cadena[1].strip() != "epsilon":
            parteUno = cadena[0].strip()
            parteDos = cadena[1].strip()        
            texto = f"{parteUno}>{parteDos} Z"
    else:
        cadena = cadena.split(">")
        parteUno = cadena[0].strip()
        parteDos = cadena[1].lstrip()
        #parteDos = parteDos.split(" ")
        texto = f"{parteUno}>{parteDos}"
    key,value = ManejadorGramatica.setProduccionInDiccionari(texto,grammar)
    if key != None and value != None:
        diccionario[key] = value
        ManejadorGramatica.updateProduccion(grammar,diccionario)
        os.system("cls")
    else:
        alertaError("No se guardo cierta parte de la Produccion")
    


def is_empty(data_structure):
    if data_structure:
        #print("No está vacía")
        return False
    else:
        #print("Está vacía")
        return True
    


