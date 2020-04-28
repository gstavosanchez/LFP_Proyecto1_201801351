from tkinter import filedialog
from tkinter import *
from io import open
import msvcrt
import os
import os.path
import sys
import msvcrt
import Menu
import ManejadorGramaticaDos
from AutomataPila import *
from PIL import Image

listaAutomataPila = []


def alerta(mensaje):
    os.system("cls")
    print("------------------------ALERTA-------------------------")
    print("|                                                     |")
    print("| Error:                                              |")
    print("| ->>No Se Realizo La Operacion                       |") 
    print(f"| -->>{mensaje}             ")
    print("|                                                     |")
    print("-------------------------------------------------------")


def get_objeto(nombre):
    nombre = nombre.strip()
    for value in listaAutomataPila:
        if value.getNombre() == nombre:
            return value
    return None

def duplicate_data(name):
    name = name.strip()
    for valor in listaAutomataPila:
        if valor.getNombre() == name:
            return True
    return False
    
def datos_Duplicados_Any_List(name,lista):
    for valor in lista:
        if name == valor:
            return True
    return False

def update_estado(automata,parametro):
    automata.setEstado(parametro)

def update_alfabeto(automata,parametro):
    automata.setAlfabeto(parametro)

def update_simbolo_pila(automata,simbolos):
    automata.setSimboloDePila(simbolos)

def update_Estado_Inicial(automata,inicio):
    automata.setEstadoInicial(inicio)
    

def update_estado_Aceptacion(automata,aceptacion):
    automata.setEstadosDeAceptacion(aceptacion)

def update_Pila(automata,pila):
    automata.setPila(pila)

def update_transicion(automata,diccionario):
    automata.setTrancisiones(diccionario)
def update_imagen(automata,direccion):
    automata.setImagen(direccion)


def new_automataPila(nombreGramatica,nombreAutomata):
    nombreGramatica = nombreGramatica.strip()
    nombreAutomata = nombreAutomata.strip()
    gramatica = ManejadorGramaticaDos.getObjeto(nombreGramatica)
    if gramatica != None:
        if duplicate_data(nombreAutomata) == False:
            nuevoAutomata = AutomataPila(nombreAutomata,[],[],"","",{},[],[],"",nombreGramatica)
            listaAutomataPila.append(nuevoAutomata)
            set_datosAutomata(nombreAutomata,nombreGramatica)
        else:
            alerta("Datos Duplicados :v")
            return False

def set_datosAutomata(nombre,gramaticaName):
    nombre = nombre.strip()
    gramaticaName = gramaticaName.strip()
    automata = get_objeto(nombre)
    gramatica = ManejadorGramaticaDos.getObjeto(gramaticaName)
    if automata != None and gramatica != None:
        listaEstados = ["i","p","q","f"]
        listaSimbolos = []
        listaTerminalGramatica = gramatica.getTerminal()
        listaNoTerminalGramatica = gramatica.getNoTerminal()
        for value in listaTerminalGramatica:
            listaSimbolos.append(value)
        for value in listaNoTerminalGramatica:
            listaSimbolos.append(value)
        listaSimbolos.append("#")
        update_alfabeto(automata,listaTerminalGramatica)
        update_simbolo_pila(automata,listaSimbolos)
        update_Estado_Inicial(automata,"i")
        update_estado_Aceptacion(automata,"f")
        update_estado(automata,listaEstados)
        if ManejadorGramaticaDos.recursivo_mejorado(gramatica) == True:
            #reajustarGramatica(gramatica.getProTransformada())
            tranciones_automata(gramatica,automata,gramatica.getProTransformada())
            get_rutaGraphviz(nombre)
        else:
            #reajustarGramatica(gramatica.getProduccion())
            tranciones_automata(gramatica,automata,gramatica.getProduccion())
            get_rutaGraphviz(nombre)
        
        
def reajustarGramatica(diccionario):
    diccTemp = {}
    for key,value in diccionario.items():
        listaTemp = []
        listaKey = value
        for cadena in listaKey:
            if cadena != "epsilon":
                if cadena.count(" ") != 0:
                    cadena = cadena.split(" ")
                    parteA = cadena[0]
                    parteB = cadena[1]
                    for i in range(len(parteA)):
                      listaTemp.append(parteA[i])
                    listaTemp.append(parteB)
                else:
                    for i in range(len(cadena)):
                        listaTemp.append(cadena[i])
            else:
                listaTemp.append(cadena)
        diccTemp[key] = listaTemp
    print(diccTemp)
                
def tranciones_automata(gramatica,automata,diccionario):
    diccAutomata = {}
    listaTerminal = gramatica.getTerminal()
    inicio = gramatica.getNoTerminalInicial()
    lam = "λ"
    trans_uno = f"i,{lam},{lam};p,#"
    trans_dos = f"p,{lam},{lam};q,{inicio}"
    #Enviar esto a al diccionario
    print(trans_uno)
    cl,val = analisis_Trancision(automata,trans_uno)
    if cl != None and val != None:
        diccAutomata[cl] = val
        update_transicion(automata,diccAutomata)
    print(trans_dos)
    cl,val = analisis_Trancision(automata,trans_dos)
    if cl != None and val != None:
        diccAutomata[cl] = val
        update_transicion(automata,diccAutomata)
    for key,value in diccionario.items():
        listaKey = value
        for cadena in listaKey:
            if cadena != "epsilon":
                if cadena.count(" ") != 0:
                    cadena = cadena.split(" ")
                    parteA = cadena[0]
                    parteB = cadena[1]
                    parte = ""
                    for i in range(len(parteA)):
                        parte += parteA[i]+" "
                    completo = f"{parte}{parteB}"
                    trans_tres = f"q,{lam},{key};q,{completo}"
                    print(trans_tres)
                    cl,val = analisis_Trancision(automata,trans_tres)
                    if cl != None and val != None:
                        diccAutomata[cl] = val
                        update_transicion(automata,diccAutomata)
                else:
                    parte =""
                    for i in range(len(cadena)):
                        parte += cadena[i]+" "
                    trans_tres = f"q,{lam},{key};q,{parte}"
                    print(trans_tres)
                    cl,val = analisis_Trancision(automata,trans_tres)
                    if cl != None and val != None:
                        diccAutomata[cl] = val
                        update_transicion(automata,diccAutomata)
            else:
                trans_tres = f"q,{lam},{key};q,{cadena}"
                print(trans_tres)
                cl,val = analisis_Trancision(automata,trans_tres)
                if cl != None and val != None:
                    diccAutomata[cl] = val
                    update_transicion(automata,diccAutomata)
    
    for valor in listaTerminal:
        trans_cuatro = f"q,{valor},{valor};q,{lam}" 
        print(trans_cuatro)
        cl,val = analisis_Trancision(automata,trans_cuatro)
        if cl != None and val != None:
            diccAutomata[cl] = val
            update_transicion(automata,diccAutomata)
        
    trans_cinco = f"q,{lam},#;f,{lam}" 
    cl,val = analisis_Trancision(automata,trans_cinco)
    if cl != None and val != None:
        diccAutomata[cl] = val
        update_transicion(automata,diccAutomata)
    #print(automata.getTrancisiones())
    os.system("cls")


def getListaInDiccionario(automata,clave):
    diccionario = automata.getTrancisiones()
    for key,value in diccionario.items():
        if clave == key:
            return value
    return None




def analisis_Trancision(automata,cadena):
    try:
        cadena = cadena.split(";")
        cadenaA = cadena[0]
        cadenaB = cadena[1]
        listaCadenaA = cadenaA.split(",")
        key = listaCadenaA[0]
        parte = ""
        for i in range(len(listaCadenaA)):
            letra = listaCadenaA[i]
            if i == len(listaCadenaA) -1 :
                parte += letra+";"
            elif i !=0:
                parte += letra+","
        nuevaCadena = parte+cadenaB
        listaTemp = getListaInDiccionario(automata,key)
        if listaTemp == None:
            listaTemp = []
            if datos_Duplicados_Any_List(nuevaCadena,listaTemp) == False:
                listaTemp.append(nuevaCadena)
                return (key,listaTemp)
            else:
                return (key,listaTemp)
        else:
            if datos_Duplicados_Any_List(nuevaCadena,listaTemp) == False:
                listaTemp.append(nuevaCadena)
                return (key,listaTemp)
            else:
                return (key,listaTemp)
    except IndexError as e:
        alerta(e)
        return (None,None)

def is_empty(data_structure):
    if data_structure:
        #print("No está vacía")
        return False
    else:
        #print("Está vacía")
        return True

def writeArchivo(texto,ruta):
    archivo  = open(f"{ruta}","a",encoding="utf-8")
    texto = f"{texto}\n"
    archivo.writelines(texto)
    archivo.close()

def wirteArvhico_ejutar(commando):
    os.system (commando)


def get_rutaGraphviz(nombre):
    nombre = nombre.strip()
    automata = get_objeto(nombre)
    if automata != None:
        root = Tk()
        root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select IMAGEN file",filetypes = (("png files","*.png"),("all files","*.*")))
        ruta = ""
        ruta = root.filename
        comando  = ""
        if is_empty(ruta.strip()) == False:
            ruta_imagen = f"{ruta}.png"
            ruta_dot = f"{ruta}.dot"
            root.destroy()
            comando = 'dot -Tpng "%s" -o "%s"'%(ruta_dot,ruta_imagen)
            #print("rutaImagen:"+ruta_imagen)
            #print("RutaDos:"+ruta_dot)
            update_imagen(automata,ruta_imagen)
            generate_Graphviz(nombre,ruta_dot)
            wirteArvhico_ejutar(comando)
        else:
            alerta("No escribio ningun nombre")
            root.destroy()
            return None
    else:
        alerta("No se encontro el automata ): ")
        return None

    
def generate_Graphviz(nombre,rutaDot):
    automata = get_objeto(nombre.strip())
    if automata != None:
        diccionario = automata.getTrancisiones()
        bloqueUno = "  R[shape=point] \n  node [shape = circle] \n  i [] \n  p [] \n  q [ height=1.7 width=1.7] \n  f [shape=doublecircle]\n"
        bloqueDos = "  rankdir=LR; \n  R -> i\n  "
        
        for key,value in diccionario.items():
            listaInKey = value
            if key == "i":
                for cadena in listaInKey:
                    cadena = cadena.replace("p,","")
                    bloqueDos += 'i -> p [label="%s"] \n  '%(cadena)
            if key == "p":
                for cadena in listaInKey:
                    cadena = cadena.replace("q,","")
                    bloqueDos += 'p -> q [label="%s"] \n  '%(cadena)
            if key == "q":
                for cadena in listaInKey:
                    if cadena.count("f") != 0:
                        cadena = cadena.replace("f,","")
                        cadena = cadena.replace("epsilon"," &epsilon; ")
                        bloqueDos += 'q -> f [label="%s"] \n  '%(cadena)
                    else:
                        cadena = cadena.replace("q,","")
                        cadena = cadena.replace("epsilon"," &epsilon; ")
                        bloqueDos += 'q -> q [label="%s"] \n  '%(cadena)
        
        texto = 'digraph G { \n \n {\n %s \n  } \n %s \n  }'%(bloqueUno,bloqueDos)
        #print(texto)
        writeArchivo(texto,rutaDot)

def mostrar_sextupla(nombre):
    nombre = nombre.strip()
    automata = get_objeto(nombre)
    if automata != None:
        alfa = get_texto(automata.getAlfabeto())
        simbol = get_texto(automata.getSimboloDePila())
        estado = get_texto(automata.getEstado())
        inic = automata.getEstadoInicial()
        aceptacion = automata.getEstadosDeAceptacion()
        transicion = get_tra(automata.getTrancisiones())
        os.system("cls")
        print("-------------------Automata de Pila--------------------")
        print(" 0.Sextupla:{S, Σ, Γ, T, L, F}")
        print(f" 1.Σ:{alfa}")
        print(f" 2.Γ:{simbol}")
        print(f" 3.S:{estado}")
        print(" 4.L:{"+inic+"}")
        print(" 5.F:{"+aceptacion+"}")
        print(" 6.T:")
        print(transicion)
        open_image(automata.getImagen())
    else:
        alerta("No se encontro el automata")

def get_texto(lista):
    texto = ""
    for i in range(len(lista)):
        leta = lista[i]
        if i == len(lista) - 1:
            texto += leta
        else:
            texto += leta+","
    textoCompleto = "{"+texto+"}"
    return textoCompleto

def get_tra(diccionario):
    texto = ""
    for key,value in diccionario.items():
        listaKey = value
        for cadena in listaKey:
            para = key+","+cadena
            texto += f"     {para}\n"
    textoCompleto = "{"+texto+"}"
    return textoCompleto

def open_image(direccion):
    try:
        ruta = direccion.strip()
        im = Image.open(ruta)
        im.show()
    except IndexError as e:
        alerta(e)
    
# Metodos para validar Cadena
def search_automataGramatica(nombre):
    nombre = nombre.strip()
    for valor in listaAutomataPila:
        if valor.getGramatica() == nombre:
            return True
    return False

def get_AutomataGramtica(nombre):
    nombre = nombre.strip()
    for valor in listaAutomataPila:
        if valor.getGramatica() == nombre:
            return valor
    return None

def getCadena():
    os.system("cls")
    print("-----------------------Validar-------------------------")
    print("| Ingrese Cadena:                                     |")
    print("-------------------------------------------------------")
    print("")
    print(">> ",end="")
    cadena = input()
    cadena = cadena.strip()
    return cadena

def validar_Cadena(nombre):
    lam = "λ"
    nombre = nombre.strip()
    automata = get_AutomataGramtica(nombre)
    if automata != None:
        entrada = getCadena()
        entradaAux = entrada
        gramatica = ManejadorGramaticaDos.getObjeto(nombre)
        inicio = gramatica.getNoTerminalInicial()
        pila = []
        x = 0
        try:
            reporte = ""
            txtPila = ""
            txtTran = ""
            pila.append(lam)
            txtPila = get_textoPila(pila)
            sacado = pila.pop()
            buscar = f"{lam},{sacado};p,#"
            estado,insertar,cadeComple = get_TrancisionPila(automata,"i",buscar)#1
            #Guardar estado anterior
            txtTran = "(i,"+cadeComple+")"
            reporte += f"{txtPila} $ {entradaAux} $ {txtTran}\n"#Cambio de estado i ->p
            #Aqui se insertar el #
            pila = insert_Pila(pila,insertar)
            # Realizar siguiente trancison p->q
            buscar = f"{lam},{lam};q,{inicio}"
            estado,insertar,cadeComple = get_TrancisionPila(automata,estado,buscar)#2
            txtPila = get_textoPila(pila)
            txtTran = "(p,"+cadeComple+")"
            reporte += f"{txtPila} $ {entradaAux} $ {txtTran}\n"
            #Insertar S a la pila
            pila = insert_Pila(pila,insertar)                    
            listaCadena = entrada.split(" ")
            print("Estado actual de la pila:",pila)
            print("Ultimo que se inserto:",insertar," Estado estoy:",estado) 
            print("Reporte:"+reporte)
            #Incia el ciclo con while, para determinar si es valida
            while True:
                if x != len(listaCadena):
                    print("x:",x)                                
                    letra = listaCadena[x]
                    #Ver el ultimo elemento de la pila
                ultima = get_ultimo(pila)
                print("------------------------------------------")
                print("Letra Actual:",letra)
                print("Ultima letra de la pila:",ultima)
                # Verificar lo que trae la ultmima posicion de la letra
                if ultima != None:
                    if ultima == "#":
                        buscar = f"{lam},{ultima};"
                        estado,insertar,cadeComple = get_TrancisionPila(automata,estado,buscar)#3
                        txtPila = get_textoPila(pila)
                        txtTran = "(q,"+cadeComple+")"
                        reporte += f"{txtPila} $ {entradaAux} $ {txtTran}\n"
                        sacado = pila.pop()
                        if estado != None and insertar != None:
                            print("Se saco de la pila:",sacado)
                            print("Estado actual de la pila:",pila)
                            print("Ultimo que se inserto:",insertar," Estado estoy:",estado)
                            print("Estado actual de la cadena:",entradaAux)
                            print("Salio por el #")
                            break
                    elif ultima != letra:
                        #Ver Cuantas coicidencias hay 
                        tran = f"{lam},{ultima};"
                        numero = get_No_repetidos(automata,tran)
                        if numero == 1:
                            #Auxiliar de insertar
                            auxInsert = get_EspecificoTrancisionPila(automata,tran)
                            # Generar Cadena para la insersion de pila
                            buscar = f"{lam},{ultima};{estado},{auxInsert}"
                            #Buscar Transicion
                            estado,insertar,cadeComple = get_TrancisionPila(automata,estado,buscar)#4
                            txtPila = get_textoPila(pila)
                            txtTran = "("+estado+","+cadeComple+")"
                            reporte += f"{txtPila} $ {entradaAux} $ {txtTran}\n"
                            #Hacer Pop de la pila
                            sacado = pila.pop()
                            if estado != None:
                                #Insertar en pila
                                pila = insert_Pila(pila,insertar)
                                print("Se saco de la pila:",sacado)
                                print("Estado actual de la pila:",pila)
                                print("Ultimo que se inserto:",insertar," Estado estoy:",estado)
                                print("Estado actual de la cadena:",entradaAux)
                            else:
                                #alerta("Se genero mal la cadena")
                                print("se genero mal la cadena")
                                break # Revisar para eliminar este brea 
                        elif numero > 1:
                            # Generar Cadena para insertar en la pila, hay mas de dos concidencias ser mas especifico,que se quiere
                            buscar = f"{lam},{ultima};{estado},{letra}"
                            estado,insertar,cadeComple = get_TrancisionPila(automata,estado,buscar)#5
                            #Guardar Reporte
                            txtPila = get_textoPila(pila)
                            txtTran = "("+estado+","+cadeComple+")"
                            reporte += f"{txtPila} $ {entradaAux} $ {txtTran}\n"
                            #Hacer Pop la Pila
                            sacado = pila.pop()
                            #Insertaren pila
                            if estado != None and insertar != None:
                                pila = insert_Pila(pila,insertar)
                                print("Se saco de la pila:",sacado)
                                print("Estado actual de la pila:",pila)
                                print("Ultimo que se inserto:",insertar," Estado estoy:",estado)
                                print("Estado actual de la cadena:",entradaAux)
                            else:
                                #alerta("Se genero mal la cadena")
                                print("-->Error: No se encontro la transicion<--")
                                print("Se saco de la pila:",sacado)
                                print("Estado actual de la pila:",pila)
                                print("Ultimo que se inserto:",insertar," Estado estoy:",estado)
                                print("Estado actual de la cadena:",entradaAux)
                                break # Revisar para eliminar este break 
                        else:
                            print("No se genero bien la consulta de las veces de repetir")
                            break      
                    elif ultima == letra:
                        buscar = f"{ultima},{ultima};"
                        estado,insertar,cadeComple = get_TrancisionPila(automata,estado,buscar)#6
                        
                        #Guardar Reporte
                        txtPila = get_textoPila(pila)
                        txtTran = "("+estado+","+cadeComple+")"
                        reporte += f"{txtPila} $ {entradaAux} $ {txtTran}\n"
                        sacado = pila.pop()
                        entradaAux = entradaAux.replace(letra,"",1)
                        print("Se saco de la pila:",sacado)
                        print("Estado actual de la pila:",pila)
                        print("Estado actual de la cadena:",entradaAux)
                        print("Estado en que estoy:",estado)
                        x +=1
                else:
                    break       
            print(reporte)       
            
        except IndexError as e:
            print(e)
            #alerta(e)
    else:
        alerta("No se encontro el Automata de Pila")


def get_TrancisionPila(automata,clave,buscado):
    diccionario = automata.getTrancisiones()
    for key,value in diccionario.items():
        if key == clave:
            lista = value
            for cadena in lista:
                if cadena.count(buscado) == 1:
                    nuevaCadena = cadena
                    nuevaCadena = nuevaCadena.strip()
                    cadena = cadena.split(";")
                    paretA = cadena[0]
                    parteB = cadena[1]
                    parteB = parteB.split(",")
                    estado = parteB[0]
                    insePila = parteB[1]
                    insePila = insePila.strip()
                    return estado,insePila,nuevaCadena
    return None,None,None

def get_EspecificoTrancisionPila(automata,buscado):
    diccionario = automata.getTrancisiones()
    for key,value in diccionario.items():
        if key == "q":
            lista = value
            for cadena in lista:
                if cadena.count(buscado) == 1:
                    nuevaCadena = cadena
                    cadena = cadena.split(";")
                    paretA = cadena[0]
                    parteB = cadena[1]
                    parteB = parteB.split(",")
                    estado = parteB[0]
                    insePila = parteB[1]
                    insePila = insePila.strip()
                    return insePila
    return None

def get_No_repetidos(automata,buscado):
    diccionario = automata.getTrancisiones()
    buscado = buscado.strip()
    x = 0
    print("buscado:"+buscado)
    for key,value in diccionario.items():
        if key == "q":
            lista = value
            for cadena in lista:
                if cadena.find(buscado) -1:
                    x +=1
    return x
                

def insert_Pila(pila,cadena):
    try:
        cadena = cadena.split(" ")
        for valor in reversed(cadena):
            #print(valor)
            pila.append(valor)
        return pila
    except IndexError as e:
        alerta(e)
        return None
    
def get_ultimo(lista):
    for i in range(len(lista)):
        if i == len(lista) - 1:
            return(lista[i])
    return None


def get_textoPila(lista):
    texto = ""
    for i in range(len(lista)):
        letra = lista[i]
        if i == len(lista) - 1:
            texto += letra
        else:
            texto += letra+" "
    return texto