import os
import sys
import msvcrt
import ManejadorAFD
import ManejadorGramatica

letra = ""

def alertaPedirDatos():
    os.system("cls")
    print("------------------------ALERTA-------------------------")
    print("| Ingrese datos:                                      |")
    print("-------------------------------------------------------")

def alertaError(mensaje):
    os.system("cls")
    print("------------------------ALERTA-------------------------")
    print("|                                                     |")
    print("| Error:                                              |")
    print("| ->>No Se Realizo La Operacion                       |") 
    print(f"| -->>{mensaje}                                    ")
    print("|                                                     |")
    print("-------------------------------------------------------")


def alertaExito(cadena,mensaje):
    os.system("cls")
    print("------------------------ALERTA-------------------------")
    print("|                                                     |")
    print("| Exito:                                              |")
    print("| ->>Se Realizo La Operacion:                         |") 
    print(f"| Cadena:{cadena}")
    print(f"| {mensaje}")
    print("|                                                      ")
    print("|                                                     |")
    print("-------------------------------------------------------")

def existAFDGramatica(nombre):
    nombre = nombre.strip()
    automata = ManejadorAFD.buscarAFD(nombre)
    gramatica = ManejadorGramatica.searchGrammar(nombre)
    if automata != None:
        return True
    elif gramatica != None:
        return True
    else:
        return False

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

def getCadena():
    os.system("cls")
    print("------------------------ALERTA-------------------------")
    print("| Ingrese Cadena:                                     |")
    print("-------------------------------------------------------")
    print("")
    print(">> ",end="")
    cadena = input()
    cadena = cadena.strip()
    return cadena
    



def getLetra(self):
    return self.letra
    
def validateCadena(name,soloValidar,forma):
    cadena = getCadena()
    cade = cadena
    name = name.strip()
    text = ""
    condicion = ""
    tipo,objeto = getObjet(name)
    if tipo != None and objeto != None:
        if tipo == "automata" and forma == "automata":
            estadoInicial = objeto.getEstadoInicial()
            estadoInicial = estadoInicial.strip()
            estadosAceptacion = objeto.getEstadosDeAceptacion()
            listaIncial = ManejadorAFD.getListDiccionario(objeto,estadoInicial)
            texto = estadoInicial
            listaTrancion = objeto.getTrancisiones()
            if estadoInicial != None and estadosAceptacion != None and listaIncial != None: 
                #print(listaTrancion)
                #print("Estado de aceptacion:",estadosAceptacion)
                #print("---------------------------------------")
                for i in range(len(cadena)):
                    valor = ""
                    if i == 0:
                        if i != len(cadena) - 1:
                            valor = getEstadoCadena(cadena[i],listaIncial)
                            destino = valor.split(" ")
                            con = destino[0]
                            destino = destino[1]
                            letra = destino
                            textoPrimero = f"{texto},{destino},{con};"
                            #print(textoPrimero)
                        else:
                            valor = getEstadoCadena(cadena[i],listaIncial)
                            destino = valor.split(" ")
                            con = destino[0]
                            destino = destino[1]
                            letra = destino
                            textoPrimero = f"{texto},{destino},{con};"
                            #print(textoPrimero)
                            if soloValidar == "validar":
                                if getEstadoAceptacion(letra,estadosAceptacion) == True:
                                    condicion = "Valida"
                                    alertaExito(cade,">> Valida")
                                    return True
                                else:
                                    condicion = "No Valida"
                                    alertaExito(cade,">> No Valida")
                                    return True
                            else:
                                if getEstadoAceptacion(letra,estadosAceptacion) == True:
                                    condicion = "Valida"
                                else:
                                    condicion = "No Valida"        
                    else :
                        if i != len(cadena) - 1 :
                            #print(f"Valor de inicio en {i} :",letra)
                            inicio = letra
                            lista = ManejadorAFD.getListDiccionario(objeto,inicio)
                            valor = getEstadoCadena(cadena[i],lista)
                            if valor != None:
                                destino = valor.split(" ")
                                con = destino[0]
                                destino = destino[1]
                                letra = destino
                                text += '%s,%s,%s; '%(inicio,destino,con)
                                #text += f"{inicio},{destino};{con}"
                        else:
                            #print(f"Valor de Fin en {i} :",letra)
                            inicio = letra
                            lista = ManejadorAFD.getListDiccionario(objeto,inicio)
                            valor = getEstadoCadena(cadena[i],lista)
                            if valor != None:
                                destino = valor.split(" ")
                                con = destino[0]
                                destino = destino[1]
                                letra = destino
                                text += '%s,%s,%s; '%(inicio,destino,con)
                                if soloValidar == "validar":
                                    if getEstadoAceptacion(letra,estadosAceptacion) == True:
                                        condicion = "Valida"
                                        alertaExito(cade,">> Valida")
                                        return True
                                    else:
                                        condicion = "No Valida"
                                        alertaExito(cade,">> No Valida")
                                        return True
                                else:
                                    if getEstadoAceptacion(letra,estadosAceptacion) == True:
                                        condicion = "Valida"
                                    else:
                                        condicion = "No Valida"
                #print("Expansion en gramatica:",textoPrimero,text," ->",condicion)
                todo = f"Ruta en AFD: {textoPrimero}{text} --> {condicion}"
                alertaExito(cade,todo)
            else:
                alertaError("Falta elmentos del AFD")           
        elif tipo == "automata" and forma == "grammar":
            estadoInicial = objeto.getEstadoInicial()
            estadoInicial = estadoInicial.strip()
            estadosAceptacion = objeto.getEstadosDeAceptacion()
            listaIncial = ManejadorAFD.getListDiccionario(objeto,estadoInicial)
            texto = estadoInicial
            listaTrancion = objeto.getTrancisiones()
            agrupacion = ""
            primerTexto = ""
            segundoTexto = ""
            condicion = ""
            eps = ""
            if estadoInicial != None and estadosAceptacion != None and listaIncial != None:
                for i in range(len(cadena)):
                    valor = ""
                    if i == 0:
                        if i != len(cadena) - 1:
                            valor = getEstadoCadena(cadena[i],listaIncial)
                            destino = valor.split(" ")
                            con = destino[0]
                            destino = destino[1]
                            agrupacion += f"{con}"
                            letra = destino
                            primerTexto = f"{texto} --> {agrupacion} {destino} --> "
                        else:
                            valor = getEstadoCadena(cadena[i],listaIncial)
                            destino = valor.split(" ")
                            con = destino[0]
                            destino = destino[1]
                            agrupacion += f"{con}"
                            letra = destino
                            primerTexto = f"{texto} --> {agrupacion} {destino} --> "                            
                            if soloValidar == "validar":
                                if getEstadoAceptacion(letra,estadosAceptacion) == True:
                                    eps = "epsilon"
                                    condicion = f"{cade}({eps})-->{cade} Valida"  
                                    alertaExito(cade,">> Valida")
                                    return True
                                else:
                                    condicion = f"{cade}({letra})-->{cade} No Valida"
                                    alertaExito(cade,">> No Valida")
                                    return True
                            else:                                
                                if getEstadoAceptacion(letra,estadosAceptacion) == True:
                                    eps = "epsilon"
                                    condicion = f"{cade}({eps})-->{cade} Valida"  
                                else:
                                    condicion = f"{cade}({letra})-->{cade} No Valida"
                    else:
                        if i != len(cadena) - 1 :
                            inicio = letra
                            lista = ManejadorAFD.getListDiccionario(objeto,inicio)
                            valor = getEstadoCadena(cadena[i],lista)
                            if valor != None:
                                destino = valor.split(" ")
                                con = destino[0]
                                agrupacion += f"{con}"
                                destino = destino[1]
                                letra = destino
                                segundoTexto += "%s %s --> "%(agrupacion,destino)
                        else:
                            inicio = letra
                            lista = ManejadorAFD.getListDiccionario(objeto,inicio)
                            valor = getEstadoCadena(cadena[i],lista)
                            if valor != None:
                                destino = valor.split(" ")
                                con = destino[0]
                                agrupacion += f"{con}"
                                destino = destino[1]
                                letra = destino
                                segundoTexto += "%s %s --> "%(agrupacion,destino)
                                
                                if soloValidar == "validar":
                                    if getEstadoAceptacion(letra,estadosAceptacion) == True:
                                        eps = "epsilon"
                                        condicion = f"{cade}({eps})-->{cade} Valida"  
                                        alertaExito(cade,">> Valida")
                                        return True
                                    else:
                                        condicion = f"{cade}({letra})-->{cade} No Valida"
                                        alertaExito(cade,">> No Valida")
                                        return True
                                else:                                
                                    if getEstadoAceptacion(letra,estadosAceptacion) == True:
                                        eps = "epsilon"
                                        condicion = f"{cade}({eps})-->{cade} Valida"  
                                    else:
                                        condicion = f"{cade}({letra})-->{cade} No Valida"
                    #print("Ruta en Gramatica: ",primerTexto,segundoTexto,condicion)
                    todo = f"Expansion en Gramatica: {primerTexto}{segundoTexto}{condicion}"
                    alertaExito(cade,todo)
            else:
                alertaError("Falta elmentos del AFD")
        elif tipo == "grammar" and forma == "grammar":
            estadoInicial = objeto.getInicio()
            estadoInicial = estadoInicial.strip()
            estadosAceptacion = objeto.getEstadosAceptacion()
            listaIncial = ManejadorGramatica.getListDiccionario(objeto,estadoInicial)
            texto = estadoInicial
            listaTrancion = objeto.getProduccion()
            agrupacion = ""
            primerTexto = ""
            segundoTexto = ""
            condicion = ""
            eps = ""
            if estadoInicial != None and estadosAceptacion != None and listaIncial != None:
                for i in range(len(cadena)):
                    valor = ""
                    if i == 0:
                        if i != len(cadena) - 1:
                            valor = getEstadoCadena(cadena[i],listaIncial)
                            destino = valor.split(" ")
                            con = destino[0]
                            destino = destino[1]
                            agrupacion += f"{con}"
                            letra = destino
                            primerTexto = f"{texto} --> {agrupacion} {destino} --> "
                        else:
                            valor = getEstadoCadena(cadena[i],listaIncial)
                            destino = valor.split(" ")
                            con = destino[0]
                            destino = destino[1]
                            agrupacion += f"{con}"
                            letra = destino
                            primerTexto = f"{texto} --> {agrupacion} {destino} --> "                            
                            if soloValidar == "validar":
                                if getEstadoAceptacion(letra,estadosAceptacion) == True:
                                    eps = "epsilon"
                                    condicion = f"{cade}({eps})-->{cade} Valida"  
                                    alertaExito(cade,">> Valida")
                                    return True
                                else:
                                    condicion = f"{cade}({letra})-->{cade} No Valida"
                                    alertaExito(cade,">> No Valida")
                                    return True
                            else:                                
                                if getEstadoAceptacion(letra,estadosAceptacion) == True:
                                    eps = "epsilon"
                                    condicion = f"{cade}({eps})-->{cade} Valida"  
                                else:
                                    condicion = f"{cade}({letra})-->{cade} No Valida"
                    else:
                        if i != len(cadena) - 1 :
                            inicio = letra
                            lista = ManejadorGramatica.getListDiccionario(objeto,inicio)
                            valor = getEstadoCadena(cadena[i],lista)
                            if valor != None:
                                destino = valor.split(" ")
                                con = destino[0]
                                agrupacion += f"{con}"
                                destino = destino[1]
                                letra = destino
                                segundoTexto += "%s %s --> "%(agrupacion,destino)
                        else:
                            inicio = letra
                            lista = ManejadorGramatica.getListDiccionario(objeto,inicio)
                            valor = getEstadoCadena(cadena[i],lista)
                            if valor != None:
                                destino = valor.split(" ")
                                con = destino[0]
                                agrupacion += f"{con}"
                                destino = destino[1]
                                letra = destino
                                segundoTexto += "%s %s --> "%(agrupacion,destino)
                                
                                if soloValidar == "validar":
                                    if getEstadoAceptacion(letra,estadosAceptacion) == True:
                                        eps = "epsilon"
                                        condicion = f"{cade}({eps})-->{cade} Valida"  
                                        alertaExito(cade,">> Valida")
                                        return True
                                    else:
                                        condicion = f"{cade}({letra})-->{cade} No Valida"
                                        alertaExito(cade,">> No Valida")
                                        return True
                                else:                                
                                    if getEstadoAceptacion(letra,estadosAceptacion) == True:
                                        eps = "epsilon"
                                        condicion = f"{cade}({eps})-->{cade} Valida"  
                                    else:
                                        condicion = f"{cade}({letra})-->{cade} No Valida"
                    #print("Ruta en Gramatica: ",primerTexto,segundoTexto,condicion)
                    todo = f"Expansion en Gramatica: {primerTexto}{segundoTexto}{condicion}"
                    alertaExito(cade,todo)
            else:
                alertaError("Falta elmentos del AFD") 
        elif tipo == "grammar" and forma == "automata":
            estadoInicial = objeto.getInicio()
            estadoInicial = estadoInicial.strip()
            estadosAceptacion = objeto.getEstadosAceptacion()
            listaIncial = ManejadorGramatica.getListDiccionario(objeto,estadoInicial)
            texto = estadoInicial
            listaTrancion = objeto.getProduccion()
            if estadoInicial != None and estadosAceptacion != None and listaIncial != None: 
                #print(listaTrancion)
                #print("Estado de aceptacion:",estadosAceptacion)
                #print("---------------------------------------")
                for i in range(len(cadena)):
                    valor = ""
                    if i == 0:
                        if i != len(cadena) - 1:
                            valor = getEstadoCadena(cadena[i],listaIncial)
                            destino = valor.split(" ")
                            con = destino[0]
                            destino = destino[1]
                            letra = destino
                            textoPrimero = f"{texto},{destino},{con};"
                            #print(textoPrimero)
                        else:
                            valor = getEstadoCadena(cadena[i],listaIncial)
                            destino = valor.split(" ")
                            con = destino[0]
                            destino = destino[1]
                            letra = destino
                            textoPrimero = f"{texto},{destino},{con};"
                            #print(textoPrimero)
                            if soloValidar == "validar":
                                if getEstadoAceptacion(letra,estadosAceptacion) == True:
                                    condicion = "Valida"
                                    alertaExito(cade,">> Valida")
                                    return True
                                else:
                                    condicion = "No Valida"
                                    alertaExito(cade,">> No Valida")
                                    return True
                            else:
                                if getEstadoAceptacion(letra,estadosAceptacion) == True:
                                    condicion = "Valida"
                                else:
                                    condicion = "No Valida"        
                    else :
                        if i != len(cadena) - 1 :
                            #print(f"Valor de inicio en {i} :",letra)
                            inicio = letra
                            lista = ManejadorGramatica.getListDiccionario(objeto,inicio)
                            valor = getEstadoCadena(cadena[i],lista)
                            if valor != None:
                                destino = valor.split(" ")
                                con = destino[0]
                                destino = destino[1]
                                letra = destino
                                text += '%s,%s,%s; '%(inicio,destino,con)
                                #text += f"{inicio},{destino};{con}"
                        else:
                            #print(f"Valor de Fin en {i} :",letra)
                            inicio = letra
                            lista = ManejadorGramatica.getListDiccionario(objeto,inicio)
                            valor = getEstadoCadena(cadena[i],lista)
                            if valor != None:
                                destino = valor.split(" ")
                                con = destino[0]
                                destino = destino[1]
                                letra = destino
                                text += '%s,%s,%s; '%(inicio,destino,con)
                                if soloValidar == "validar":
                                    if getEstadoAceptacion(letra,estadosAceptacion) == True:
                                        condicion = "Valida"
                                        alertaExito(cade,">> Valida")
                                        return True
                                    else:
                                        condicion = "No Valida"
                                        alertaExito(cade,">> No Valida")
                                        return True
                                else:
                                    if getEstadoAceptacion(letra,estadosAceptacion) == True:
                                        condicion = "Valida"
                                    else:
                                        condicion = "No Valida"
                #print("Expansion en gramatica:",textoPrimero,text," ->",condicion)
                todo = f"Ruta en AFD: {textoPrimero}{text} --> {condicion}"
                alertaExito(cade,todo)
            else:
                alertaError("Falta elmentos del AFD")
    else:
        alertaError("No se encontro el AFD o la Gramatica")
        
   
  
  
  

def getEstadoAceptacion(letra,lista):
    for value in lista:
        if value.strip() == letra.strip():
            return True
    return False
     
        
def getCadenaEnFor(cadena,listaIncial):
    for i in range(len(cadena)):
        for x in range(len(listaIncial)):
                valor = listaIncial[x]
                if valor.find(cadena[i]) != -1:
                    #print("Cadena de lista:",valor, "letra:",cadena[i])
                    return(cadena[i],valor)
                
def getEstadoCadena(letra,listadoIncial):
    #print("Letra:",letra)
    #print("Listado:",listadoIncial)
    for x in range(len(listadoIncial)):
        valor = listadoIncial[x]
        if valor.find(letra) != -1:
            #print("Valor a retornar:",valor)
            return(valor)
    return None
    