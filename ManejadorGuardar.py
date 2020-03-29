from tkinter import filedialog
from tkinter import *
from io import open
import os
import os.path
import sys
import msvcrt
import ManejadorGramatica
import ManejadorAFD
from reportlab.pdfgen import canvas 
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

def alertaError(mensaje):
    os.system("cls")
    print("------------------------ALERTA-------------------------")
    print("|                                                     |")
    print("| Error:                                              |")
    print("| ->>No Se Realizo La Operacion                       |") 
    print(f"| -->>{mensaje}                  ")
    print("|                                                     |")
    print("-------------------------------------------------------")

def alertaExito(mensaje):
    os.system("cls")
    print("------------------------ALERTA-------------------------")
    print("|                                                     |")
    print("| Operacion:                                          |")
    print(f"| ->>{mensaje}")
    print("|                                                      ")
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
    
def wirteArchivoGraphi(texto,ruta,commando):
    writeArchivo(texto,ruta)
    os.system (commando)

def getRutaGraphiz(nombre):
    tipo,objeto = getObjet(nombre.strip())
    if tipo != None and objeto != None:
        root = Tk()
        root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select IMAGEN file",filetypes = (("png files","*.png"),("all files","*.*")))
        ruta = root.filename
        texto  = ""
        if is_empty(ruta.strip()) == False:
            rutaImagen = f"{ruta}.png"
            rutaDot = f"{ruta}.dot"
            rutaCMD = f"{ruta}.cmd"
            root.destroy()
            texto = 'cd %s \n dot -Tpng "%s" -o "%s"'%(ruta,rutaDot,rutaImagen)
            prueba = 'dot -Tpng "%s" -o "%s"'%(rutaDot,rutaImagen)
            generateGraphiz(nombre,rutaDot)
            wirteArchivoGraphi(texto,rutaCMD,prueba)
            return tipo,objeto,rutaImagen
        else:
            alertaError("No escribio ningun nombre")
            root.destroy()
            return None,None,None
    else:
        alertaError("No encontro el afd o gramatica")
        return None,None,None
    
                


def generateGraphiz(nombre,rutaDot):
    tipo,objeto = getObjet(nombre.strip())
    if tipo != None and objeto != None:
        bloqueUno = ""
        bloqueDos = ""
        texto = ""
        inicioCadena = ""
        if tipo == "automata":
            listaEstados = objeto.getEstado()
            listEstadoAceptacion = objeto.getEstadosDeAceptacion()
            diccionario = objeto.getTrancisiones()
            estadoInicial = objeto.getEstadoInicial()
            
            for est in listaEstados:
                if searchInListAceptacion(est,listEstadoAceptacion) == True:
                    bloqueUno += '  %s [shape=doublecircle] \n'%(est)
                elif est == estadoInicial:
                    bloqueUno += '  R [shape=point] \n'
                    inicioCadena = f"  R -> {estadoInicial}\n"
                else:
                    bloqueUno += f"  {est} [] \n"
            
            for key,value in diccionario.items():
                for listCadena in value:
                    cadena = listCadena.split(" ")
                    alfabeto = cadena[0]
                    estado = cadena[1]
                    
                    bloqueDos += '  %s -> %s [label="%s"] \n'%(key,estado,alfabeto)

            texto = 'digraph G { \n \n {\n%s \n  } \n%s %s \n  }'%(bloqueUno,inicioCadena,bloqueDos)
            writeArchivo(texto,rutaDot)
            
        elif tipo == "grammar":
            listaEstados = objeto.getNoTerminal()
            listEstadoAceptacion = objeto.getEstadosAceptacion()
            diccionario = objeto.getProduccion()
            estadoInicial = objeto.getInicio()
            
            for est in listaEstados:
                if searchInListAceptacion(est,listEstadoAceptacion) == True:
                    bloqueUno += '  %s [shape=doublecircle] \n'%(est)
                elif est == estadoInicial:
                    bloqueUno += '  R [shape=point] \n'
                    inicioCadena = f"  R -> {estadoInicial}\n"
                else:
                    bloqueUno += f"  {est} [] \n"
            
            for key,value in diccionario.items():
                for listCadena in value:
                    if listCadena != "epsilon":
                        cadena = listCadena.split(" ")
                        alfabeto = cadena[0]
                        estado = cadena[1]
                        bloqueDos += '  %s -> %s [label="%s"] \n'%(key,estado,alfabeto)
                
            texto = 'digraph G { \n \n {\n%s \n  } \n%s %s \n  }'%(bloqueUno,inicioCadena,bloqueDos)
            writeArchivo(texto,rutaDot)
                        
                        
            
        

        
def generatePDF(name):
    alertaExito("Ingrese el nombre para el pdf")
    root = Tk()
    root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file PFD",filetypes = (("PDF files","*.pdf"),("all files","*.*")))
    ruta = root.filename
    
    if is_empty(ruta.strip()) == False:
        rutaPFD = f"{ruta}.pdf"
        root.destroy()
    else:
        alertaError("No escribio ningun nombre")
        root.destroy()
    if is_empty(rutaPFD.strip()) == False:
        alertaExito("Ingrese el nombre para la imagen de Graphviz")
        tipo,objeto,rutaImagen = getRutaGraphiz(name.strip())
        if tipo != None and objeto != None and rutaImagen != None:
            if tipo == "automata":
                fileName = rutaPFD
                documentTitle = 'Document title!'
                title = "Reporte de automata"
                nameAuto = objeto.getNombre() 
                subTitle = f"Nombre: {nameAuto}"
                estados = objeto.getEstado()
                alfabeto = objeto.getAlfabeto()
                estadoInicial = objeto.getEstadoInicial()
                estaodsAceptacion = objeto.getEstadosDeAceptacion()
                cadena = objeto.getCadena()
                cadenaValida = objeto.getCadenaValida()
                cadenaNoValida = objeto.getCadenaNoValida()
                tipoAfd = "~ AFD:"
                alfa = f"  > Alfabeto: {alfabeto}"
                est = f"  > Estados: {estados}"
                estInicial = f"  > Estado Inicial: {estadoInicial}"
                estAceptacion = f"  > Estados de Aceptacion: {estaodsAceptacion}"
                
                cadenaTexto = getCadenaList(cadena)
                cadenaNoValidaTexto = getCadenaList(cadenaNoValida)
                cadenaValidaTexto = getCadenaList(cadenaValida)

                textLines = [tipoAfd,
                             alfa,
                             est,
                             estInicial,
                             estAceptacion,
                             '~ Cadena Evaludas:',
                             cadenaTexto,
                             '~ Cadena Validas:',
                             cadenaValidaTexto,
                             '~ Cadena No Validas:',
                             cadenaNoValidaTexto]
                image = rutaImagen
                pdf = canvas.Canvas(fileName)
                pdf.setTitle(documentTitle)
                pdfmetrics.registerFont(TTFont('abc', 'SakBunderan.ttf'))
                pdf.setFont('abc', 36)
                pdf.drawCentredString(300, 770, title)
                #----------------------------------
                #Sub titulo para el reporte
                pdf.setFillColorRGB(0, 0, 0)
                pdf.setFont("Courier-Bold", 24)
                pdf.drawCentredString(125,720, subTitle)
                pdf.line(30, 710, 550, 710)
                text = pdf.beginText(40, 680)
                text.setFont("Courier", 14)
                text.setFillColor(colors.black)
                # for i in range(len(textLines)):
                #     te = textLines[i]
                #     if te.find("/n") != -1:
                #         textLines[i] = textLines[i].replace("/n","")
                #         textLines.append('') 
                
                for line in textLines:
                     text.textLine(line)
                pdf.drawText(text)
                pdf.drawCentredString(120,275, "AFD:")
                pdf.drawInlineImage(image, 120, 100,150,175)
                pdf.save()
            elif tipo == "grammar":
                fileName = rutaPFD
                documentTitle = 'Document title!'
                title = "Reporte de Gramatica"
                nameAuto = objeto.getNombre() 
                subTitle = f"Nombre: {nameAuto}"
                estados = objeto.getNoTerminal()
                alfabeto = objeto.getTerminal()
                estadoInicial = objeto.getInicio()
                estaodsAceptacion = objeto.getEstadosAceptacion()
                cadena = objeto.getCadena()
                cadenaValida = objeto.getCadenaValida()
                cadenaNoValida = objeto.getCadenaNoValida()
                tipoAfd = "~ AFD:"
                alfa = f"  > Alfabeto: {alfabeto}"
                est = f"  > Estados: {estados}"
                estInicial = f"  > Estado Inicial: {estadoInicial}"
                estAceptacion = f"  > Estados de Aceptacion: {estaodsAceptacion}"
                
                cadenaTexto = getCadenaList(cadena)
                cadenaNoValidaTexto = getCadenaList(cadenaNoValida)
                cadenaValidaTexto = getCadenaList(cadenaValida)
                textLines = [tipoAfd,
                             alfa,
                             est,
                             estInicial,
                             estAceptacion,
                             '~ Cadena Evaludas:',
                             cadenaTexto,
                             '~ Cadena Validas:',
                             cadenaValidaTexto,
                             '~ Cadena No Validas:',
                             cadenaNoValidaTexto]
                image = rutaImagen
                pdf = canvas.Canvas(fileName)
                pdf.setTitle(documentTitle)
                pdfmetrics.registerFont(TTFont('abc', 'SakBunderan.ttf'))
                pdf.setFont('abc', 36)
                pdf.drawCentredString(300, 770, title)
                #----------------------------------
                #Sub titulo para el reporte
                pdf.setFillColorRGB(0, 0, 0)
                pdf.setFont("Courier-Bold", 24)
                pdf.drawCentredString(125,720, subTitle)
                pdf.line(30, 710, 550, 710)
                text = pdf.beginText(40, 680)
                text.setFont("Courier", 14)
                text.setFillColor(colors.black)
                # for i in range(len(textLines)):
                #     te = textLines[i]
                #     if te.find("/n") != -1:
                #         textLines[i] = textLines[i].replace("/n","")
                #         textLines.append('') 
                
                for line in textLines:
                     text.textLine(line)
                pdf.drawText(text)
                pdf.drawCentredString(120,275, "AFD:")
                pdf.drawInlineImage(image, 120, 100,150,175)
                pdf.save()
                
                
            
            


def getCadenaList(lista):
    texto = ""
    if lista != None or len(lista) - 1 != -1:
        for value in lista:
            texto += f"  > {value} /n"
        return texto
    else:
        texto = "--"
        return texto