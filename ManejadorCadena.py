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
    try:
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
                textoPrimero = ""
                listaCadena = objeto.getCadena()
                listCadenaValida = objeto.getCadenaValida()
                listCadenaNoValida = objeto.getCadenaNoValida()
                if estadoInicial != None and estadosAceptacion != None and listaIncial != None: 
                    #print(listaTrancion)
                    #print("Estado de aceptacion:",estadosAceptacion)
                    #print("---------------------------------------")
                    for i in range(len(cadena)):
                        valor = ""
                        if i == 0:
                            if i != len(cadena) - 1:
                                valor = getEstadoCadena(cadena[i],listaIncial)
                                if valor != None:
                                    destino = valor.split(" ")
                                    con = destino[0]
                                    destino = destino[1]
                                    letra = destino
                                    textoPrimero = f"{texto},{destino},{con};"
                                    #print(textoPrimero)
                            else:
                                valor = getEstadoCadena(cadena[i],listaIncial)
                                if valor != None:
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
                                            agregar = f"{cade} {condicion}"
                                            listaCadena.append(agregar)
                                            listCadenaValida.append(cade)
                                            return True
                                        else:
                                            condicion = "No Valida"
                                            alertaExito(cade,">> No Valida")
                                            agregar = f"{cade} {condicion}"
                                            listaCadena.append(agregar)
                                            listCadenaNoValida.append(cade)
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
                                            agregar = f"{cade} {condicion}"
                                            listaCadena.append(agregar)
                                            listCadenaValida.append(cade)
                                            return True
                                        else:
                                            condicion = "No Valida"
                                            alertaExito(cade,">> No Valida")
                                            agregar = f"{cade} {condicion}"
                                            listaCadena.append(agregar)
                                            listCadenaNoValida.append(cade)
                                            return True
                                    else:
                                        if getEstadoAceptacion(letra,estadosAceptacion) == True:
                                            condicion = "Valida"
                                        else:
                                            condicion = "No Valida"
                    #print("Expansion en gramatica:",textoPrimero,text," ->",condicion)
                    todo = f"Ruta en AFD: {textoPrimero}{text} --> {condicion}"
                    alertaExito(cade,todo)
                    if condicion == "Valida":
                        agregar = f"{cade} Valida"
                        listaCadena.append(agregar)
                        listCadenaValida.append(cade)
                    elif condicion == "No Valida":
                        agregar = f"{cade} No Valida"
                        listaCadena.append(agregar)
                        listCadenaNoValida.append(cade)
                    ManejadorAFD.updateCadena(objeto,listaCadena)
                    ManejadorAFD.updateCadenaValida(objeto,listCadenaValida)
                    ManejadorAFD.updateCadenaNoValida(objeto,listCadenaNoValida)
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
                condicionActual = ""
                listaCadena = objeto.getCadena()
                listCadenaValida = objeto.getCadenaValida()
                listCadenaNoValida = objeto.getCadenaNoValida()
                if estadoInicial != None and estadosAceptacion != None and listaIncial != None:
                    for i in range(len(cadena)):
                        valor = ""
                        if i == 0:
                            if i != len(cadena) - 1:
                                valor = getEstadoCadena(cadena[i],listaIncial)
                                if valor != None:
                                    destino = valor.split(" ")
                                    con = destino[0]
                                    destino = destino[1]
                                    agrupacion += f"{con}"
                                    letra = destino
                                    primerTexto = f"{texto} --> {agrupacion} {destino} --> "
                            else:
                                valor = getEstadoCadena(cadena[i],listaIncial)
                                if valor != None:
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
                                            condicionActual = "Valida"
                                            agregar = f"{cade} {condicionActual}"
                                            listaCadena.append(agregar)
                                            listCadenaValida.append(cade)
                                            return True
                                        else:
                                            condicion = f"{cade}({letra})-->{cade} No Valida"
                                            alertaExito(cade,">> No Valida")
                                            condicionActual = "No Valida"
                                            agregar = f"{cade} {condicionActual}"
                                            listaCadena.append(agregar)
                                            listCadenaNoValida.append(cade)
                                            return True
                                    else:                                
                                        if getEstadoAceptacion(letra,estadosAceptacion) == True:
                                            eps = "epsilon"
                                            condicion = f"{cade}({eps})-->{cade} Valida"
                                            condicionActual = "Valida"  
                                        else:
                                            condicion = f"{cade}({letra})-->{cade} No Valida"
                                            condicionActual = "No Valida"
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
                                            condicionActual = "Valida"
                                            agregar = f"{cade} {condicionActual}"
                                            listaCadena.append(agregar)
                                            listCadenaValida.append(cade)
                                            return True
                                        else:
                                            condicion = f"{cade}({letra})-->{cade} No Valida"
                                            alertaExito(cade,">> No Valida")
                                            condicionActual = "No Valida"
                                            agregar = f"{cade} {condicionActual}"
                                            listaCadena.append(agregar)
                                            listCadenaNoValida.append(cade)
                                            return True
                                    else:                                
                                        if getEstadoAceptacion(letra,estadosAceptacion) == True:
                                            eps = "epsilon"
                                            condicion = f"{cade}({eps})-->{cade} Valida"
                                            condicionActual = "Valida"  
                                        else:
                                            condicion = f"{cade}({letra})-->{cade} No Valida"
                                            condicionActual = "No Valida"
                        #print("Ruta en Gramatica: ",primerTexto,segundoTexto,condicion)
                        todo = f"Expansion en Gramatica: {primerTexto}{segundoTexto}{condicion}"
                        alertaExito(cade,todo)
                        if condicionActual == "Valida":
                            agregar = f"{cade} Valida"
                            listaCadena.append(agregar)
                            listCadenaValida.append(cade)
                        elif condicionActual == "No Valida":
                            agregar = f"{cade} No Valida"
                            listaCadena.append(agregar)
                            listCadenaNoValida.append(cade)
                        ManejadorAFD.updateCadena(objeto,listaCadena)
                        ManejadorAFD.updateCadenaValida(objeto,listCadenaValida)
                        ManejadorAFD.updateCadenaNoValida(objeto,listCadenaNoValida)
                        
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
                condicionActual = ""
                listaCadena = objeto.getCadena()
                listCadenaValida = objeto.getCadenaValida()
                listCadenaNoValida = objeto.getCadenaNoValida()
                if estadoInicial != None and estadosAceptacion != None and listaIncial != None:
                    for i in range(len(cadena)):
                        valor = ""
                        if i == 0:
                            if i != len(cadena) - 1:
                                valor = getEstadoCadena(cadena[i],listaIncial)
                                if valor != None:
                                    destino = valor.split(" ")
                                    con = destino[0]
                                    destino = destino[1]
                                    agrupacion += f"{con}"
                                    letra = destino
                                    primerTexto = f"{texto} --> {agrupacion} {destino} --> "
                            else:
                                valor = getEstadoCadena(cadena[i],listaIncial)
                                if valor != None:
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
                                            condicionActual = "Valida"
                                            agregar = f"{cade} {condicionActual}"
                                            listaCadena.append(agregar)
                                            listCadenaValida.append(cade)
                                            return True
                                        else:
                                            condicion = f"{cade}({letra})-->{cade} No Valida"
                                            alertaExito(cade,">> No Valida")
                                            condicionActual = "No Valida"
                                            agregar = f"{cade} {condicionActual}"
                                            listaCadena.append(agregar)
                                            listCadenaNoValida.append(cade)
                                            return True
                                    else:                                
                                        if getEstadoAceptacion(letra,estadosAceptacion) == True:
                                            eps = "epsilon"
                                            condicion = f"{cade}({eps})-->{cade} Valida"
                                            condicionActual = "Valida"  
                                        else:
                                            condicion = f"{cade}({letra})-->{cade} No Valida"
                                            condicionActual = "No Valida"
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
                                            condicionActual = "Valida"
                                            agregar = f"{cade} {condicionActual}"
                                            listaCadena.append(agregar)
                                            listCadenaValida.append(cade)
                                            return True
                                        else:
                                            condicion = f"{cade}({letra})-->{cade} No Valida"
                                            alertaExito(cade,">> No Valida")
                                            condicionActual = "No Valida"
                                            agregar = f"{cade} {condicionActual}"
                                            listaCadena.append(agregar)
                                            listCadenaNoValida.append(cade)
                                            return True
                                    else:                                
                                        if getEstadoAceptacion(letra,estadosAceptacion) == True:
                                            eps = "epsilon"
                                            condicion = f"{cade}({eps})-->{cade} Valida"  
                                            condicionActual = "Valida"
                                        else:
                                            condicion = f"{cade}({letra})-->{cade} No Valida"
                                            condicionActual = "No Valida"
                        #print("Ruta en Gramatica: ",primerTexto,segundoTexto,condicion)
                        todo = f"Expansion en Gramatica: {primerTexto}{segundoTexto}{condicion}"
                        alertaExito(cade,todo)
                        if condicionActual == "Valida":
                            agregar = f"{cade} Valida"
                            listaCadena.append(agregar)
                            listCadenaValida.append(cade)
                        elif condicionActual == "No Valida":
                            agregar = f"{cade} No Valida"
                            listaCadena.append(agregar)
                            listCadenaNoValida.append(cade)
                        ManejadorGramatica.updateCadena(objeto,listaCadena)
                        ManejadorGramatica.updateCadenaValida(objeto,listCadenaValida)
                        ManejadorGramatica.updateCadenaNoValida(objeto,listCadenaNoValida)
                else:
                    alertaError("Falta elmentos del AFD") 
            elif tipo == "grammar" and forma == "automata":
                estadoInicial = objeto.getInicio()
                estadoInicial = estadoInicial.strip()
                estadosAceptacion = objeto.getEstadosAceptacion()
                listaIncial = ManejadorGramatica.getListDiccionario(objeto,estadoInicial)
                texto = estadoInicial
                listaTrancion = objeto.getProduccion()
                listaCadena = objeto.getCadena()
                listCadenaValida = objeto.getCadenaValida()
                listCadenaNoValida = objeto.getCadenaNoValida()
                if estadoInicial != None and estadosAceptacion != None and listaIncial != None: 
                    #print(listaTrancion)
                    #print("Estado de aceptacion:",estadosAceptacion)
                    #print("---------------------------------------")
                    for i in range(len(cadena)):
                        valor = ""
                        if i == 0:
                            if i != len(cadena) - 1:
                                valor = getEstadoCadena(cadena[i],listaIncial)
                                if valor != None:
                                    destino = valor.split(" ")
                                    con = destino[0]
                                    destino = destino[1]
                                    letra = destino
                                    textoPrimero = f"{texto},{destino},{con};"
                                    #print(textoPrimero)
                            else:
                                valor = getEstadoCadena(cadena[i],listaIncial)
                                if valor != None:
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
                                            agregar = f"{cade} {condicion}"
                                            listaCadena.append(agregar)
                                            listCadenaValida.append(cade)
                                            
                                            return True
                                        else:
                                            condicion = "No Valida"
                                            alertaExito(cade,">> No Valida")
                                            agregar = f"{cade} {condicion}"
                                            listaCadena.append(agregar)
                                            listCadenaNoValida.append(cade)
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
                                            agregar = f"{cade} {condicion}"
                                            listaCadena.append(agregar)
                                            listCadenaValida.append(cade)
                                            return True
                                        else:
                                            condicion = "No Valida"
                                            alertaExito(cade,">> No Valida")
                                            agregar = f"{cade} {condicion}"
                                            listaCadena.append(agregar)
                                            listCadenaNoValida.append(cade)
                                            return True
                                    else:
                                        if getEstadoAceptacion(letra,estadosAceptacion) == True:
                                            condicion = "Valida"
                                        else:
                                            condicion = "No Valida"
                    #print("Expansion en gramatica:",textoPrimero,text," ->",condicion)
                    todo = f"Ruta en AFD: {textoPrimero}{text} --> {condicion}"
                    alertaExito(cade,todo)
                    if condicion == "Valida":
                        agregar = f"{cade} Valida"
                        listaCadena.append(agregar)
                        listCadenaValida.append(cade)
                    else:
                        agregar = f"{cade} No Valida"
                        listaCadena.append(agregar)
                        listCadenaNoValida.append(cade)
                    ManejadorGramatica.updateCadena(objeto,listaCadena)
                    ManejadorGramatica.updateCadenaValida(objeto,listCadenaValida)
                    ManejadorGramatica.updateCadenaNoValida(objeto,listCadenaNoValida)
                    
                else:
                    alertaError("Falta elmentos del AFD")
        else:
            alertaError("No se encontro el AFD o la Gramatica")
    except IndexError as e:
        alertaError(e)
    
        
   
  
  
  

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
    