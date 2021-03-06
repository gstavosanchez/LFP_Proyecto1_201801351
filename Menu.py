import os
import ManejadorAFD
import ManejadorGramatica
import ManejadorCadena
import ManejadorArchivo
import ManejadorArchGramar
import ManejadorGuardar
import ManejadorGramaticaDos
import ManejadorAutomaPila

def menuMain():
    while True:
        print("-------------------Menu Principal----------------------")
        print("|                                                     |")
        print("| 1.Crear AFD                                         |")
        print("| 2.Crear Gramatica                                   |")
        print("| 3.Evauluar Cadena                                   |")
        print("| 4.Reportes                                          |")
        print("| 5.Cargar Archivo de Entrada                         |")
        print("| 6.Guardar                                           |")
        print("| 7.Gramatica Tipo Dos                                |")
        print("|   SALIR                                             |")
        print("|                                                     |")
        print("-------------------------------------------------------")
        print("")
        print(">> ",end="")
        opcion = input()
        opcion = opcion.strip()
        if opcion == "1":
            os.system("cls")
            menuAFD()
        elif opcion == "2":
            os.system("cls")
            menuGramatica()
        elif opcion =="3":
            os.system("cls")
            menuEvaluarCadena()
        elif opcion == "4":
            os.system("cls")
            getReporteIncio()
        elif opcion == "5":
            os.system("cls")
            menuArchivo()
        elif opcion == "6":
            os.system("cls")
            menuGuardar()
        elif opcion == "7":
            os.system("cls")
            menuGramticaTiDos()
        elif opcion.lower() == "salir":
            os.system("cls")
            print("¿Seguro que desea Salir ?")
            print(">> ",end="")
            op = input()
            op = op.strip()
            if op.lower() == "si":
                break
            else:
                os.system("cls")
        else:
            os.system("cls")

def setNombreAFD():
    print("Ingrese el nombre de AFD")
    print(">> ",end="")
    nombre = input()
    nombre = nombre.strip()
    os.system("cls")
    return nombre


def menuAFD():
    nombre = setNombreAFD()
    if nombre != "update":
        if ManejadorAFD.newAFD(nombre) == True:
            while True:
                print("-----------------------Menu AFD------------------------")
                print("|                                                     |")
                print("| 1.Ingresar Estados                                  |")
                print("| 2.Ingresar Alfabeto                                 |")
                print("| 3.Estado Inicial                                    |")
                print("| 4.Estado Aceptacion                                 |")
                print("| 5.Transiciones                                      |")
                print("| 6.Ayuda                                             |")
                print("|   SALIR                                             |")
                print("|                                                     |")
                print("-------------------------------------------------------")
                print("")
                print(">> ",end="")
                opcion = input()
                opcion = opcion.strip()
                if opcion == "1":
                    os.system("cls")
                    ManejadorAFD.setEstadosUpdate(nombre)
                elif opcion == "2":
                    os.system("cls")
                    ManejadorAFD.setAlfabeto(nombre)
                elif opcion =="3":
                    os.system("cls")
                    ManejadorAFD.setEstadoInicialAFD(nombre)
                elif opcion == "4":
                    os.system("cls")
                    ManejadorAFD.setEstadoAceptacionAFD(nombre)
                elif opcion == "5":
                    os.system("cls")
                    menuTransicion(nombre)
                elif opcion == "6":
                    os.system("cls")
                    ManejadorAFD.helpCaratula()
                    ManejadorAFD.help()
                elif opcion == "ver":
                    os.system("cls")
                    ManejadorAFD.getAFD(nombre)
                elif opcion.lower() == "salir":
                    os.system("cls")
                    break
                else:
                    os.system("cls")
        else:
            menuMain()
    else:
        nombre = setNombreAFD()
        nombre = nombre.strip()
        buscado = ManejadorAFD.buscarAFD(nombre)
        if buscado != None:
            while True:
                    print("---------------------Menu AFD UPDATE-------------------")
                    print("|                                                     |")
                    print("| 1.Ingresar Estados                                  |")
                    print("| 2.Ingresar Alfabeto                                 |")
                    print("| 3.Estado Inicial                                    |")
                    print("| 4.Estado Aceptacion                                 |")
                    print("| 5.Transiciones                                      |")
                    print("| 6.Ayuda                                             |")
                    print("|   SALIR                                             |")
                    print("|                                                     |")
                    print("-------------------------------------------------------")
                    print("")
                    print(">> ",end="")
                    opcion = input()
                    opcion = opcion.strip()
                    if opcion == "1":
                        os.system("cls")
                        ManejadorAFD.setEstadosUpdate(nombre)
                    elif opcion == "2":
                        os.system("cls")
                        ManejadorAFD.setAlfabeto(nombre)
                    elif opcion =="3":
                        os.system("cls")
                        ManejadorAFD.setEstadoInicialAFD(nombre)
                    elif opcion == "4":
                        os.system("cls")
                        ManejadorAFD.setEstadoAceptacionAFD(nombre)
                    elif opcion == "5":
                        os.system("cls")
                        menuTransicion(nombre)
                    elif opcion == "6":
                        os.system("cls")
                        ManejadorAFD.helpCaratula()
                        ManejadorAFD.help()
                    elif opcion == "ver":
                        os.system("cls")
                        ManejadorAFD.getAFD(nombre)
                    elif opcion.lower() == "salir":
                        os.system("cls")
                        break
                    else:
                        os.system("cls")
        else:
            menuAFD()


def menuTransicion(nombre):
    while True:
        print("-------------------Menu Transiciones-------------------")
        print("|                                                     |")
        print("| 1.Modo No.1                                         |")
        print("| 2.Modo No.2                                         |")
        print("|   SALIR                                             |")
        print("|                                                     |")
        print("-------------------------------------------------------")
        print("")
        print(">> ",end="")
        opcion = input()
        opcion = opcion.strip()
        if opcion == "1":
            os.system("cls")
            ManejadorAFD.modoUnoTrancision(nombre)
        elif opcion == "2":
            os.system("cls")
            ManejadorAFD.modoDosTrasiciones(nombre)
        elif opcion.lower()== "salir":
            os.system("cls")
            break
        else:
            os.system("cls")

def setNombreGramatica():
    print("Ingrese el nombre la Gramatica")
    print(">> ",end="")
    nombre = input()
    nombre = nombre.strip()
    os.system("cls")
    return nombre

def menuGramatica():
    nombre = setNombreGramatica()
    if nombre != "update":
        if ManejadorGramatica.newGramatica(nombre) == True:
            while True:
                print("---------------------Menu Gramatica--------------------")
                print("|                                                     |")
                print("| 1.Ingresar NT                                       |")
                print("| 2.Ingresar Terminales                               |")
                print("| 3.NT Inicial                                        |")
                print("| 4.Producciones                                      |")
                print("| 5.Mostar gramatica y Transformada                   |")
                print("| 6.Ayuda                                             |")
                print("|   SALIR                                             |")
                print("|                                                     |")
                print("-------------------------------------------------------")
                print("")
                print(">> ",end="")
                opcion = input()
                opcion = opcion.strip()
                if opcion == "1":
                    os.system("cls")
                    ManejadorGramatica.setNewNoTerminal(nombre)
                elif opcion == "2":
                    os.system("cls")
                    ManejadorGramatica.setNewTerminal(nombre)
                elif opcion == "3":
                    os.system("cls")
                    ManejadorGramatica.setNewNTInicial(nombre)
                elif opcion == "4":
                    os.system("cls")
                    ManejadorGramatica.setNewProduccion(nombre)
                elif opcion == "5":
                    pass
                elif opcion == "6":
                    pass
                elif opcion == "ver":
                    os.system("cls")
                    ManejadorGramatica.getGrammar(nombre)
                elif opcion.lower() == "salir":
                    os.system("cls")
                    break
                else:
                    os.system("cls")
        else:
            menuMain()
    else:
        nombre = setNombreGramatica()
        nombre = nombre.strip()
        buscado = ManejadorGramatica.searchGrammar(nombre)
        if buscado != None:
            while True:
                print("---------------Menu Gramatica UPDATE------------------")
                print("|                                                     |")
                print("| 1.Ingresar NT                                       |")
                print("| 2.Ingresar Terminales                               |")
                print("| 3.NT Inicial                                        |")
                print("| 4.Producciones                                      |")
                print("| 5.Mostar gramatica y Transformada                   |")
                print("| 6.Ayuda                                             |")
                print("|   SALIR                                             |")
                print("|                                                     |")
                print("-------------------------------------------------------")
                print("")
                print(">> ",end="")
                opcion = input()
                opcion = opcion.strip()
                if opcion == "1":
                    os.system("cls")
                    ManejadorGramatica.setNewNoTerminal(nombre)
                elif opcion == "2":
                    os.system("cls")
                    ManejadorGramatica.setNewTerminal(nombre)
                elif opcion == "3":
                    os.system("cls")
                    ManejadorGramatica.setNewNTInicial(nombre)
                elif opcion == "4":
                    os.system("cls")
                    ManejadorGramatica.setNewProduccion(nombre)
                elif opcion == "5":
                    pass
                elif opcion == "6":
                    pass
                elif opcion.lower() == "ver":
                    os.system("cls")
                    ManejadorGramatica.getGrammar(nombre)
                elif opcion.lower() == "salir":
                    os.system("cls")
                    break
                else:
                    os.system("cls")
        else:
            menuGramatica()


def getReporteIncio():
    nombre = setNombreGramaticaAFD()
    if is_empty(nombre.strip()) == False:
        if ManejadorCadena.existAFDGramatica(nombre.strip()) == True:
            ManejadorGuardar.generatePDF(nombre.strip())
         

def setNombreGramaticaAFD():
    print("Ingrese el nombre la Gramatica o AFD")
    print(">> ",end="")
    nombre = input()
    nombre = nombre.strip()
    os.system("cls")
    return nombre


def menuEvaluarCadena():
    nombre = setNombreGramaticaAFD()
    if ManejadorCadena.existAFDGramatica(nombre) == True:
        while True:
            print("-----------------Menu Evaluar Cadena-------------------")
            print("|                                                     |")
            print("| 1.Solo Validar                                      |")
            print("| 2.Ruta en AFD                                       |")
            print("| 3.Expandir con Gramatica                            |")
            print("| 4.Ayuda                                             |")
            print("|   SALIR                                             |")
            print("|                                                     |")
            print("-------------------------------------------------------")
            print("")
            print(">> ",end="")
            opcion = input()
            opcion = opcion.strip()
            if opcion == "1":
                os.system("cls")
                ManejadorCadena.validateCadena(nombre,"validar","automata")
            elif opcion == "2":
                os.system("cls")
                #ManejadorCadena.validateCadena(nombre,"","grammar")
                ManejadorCadena.validateCadena(nombre,"","automata")
            elif opcion == "3":
                os.system("cls")
                ManejadorCadena.validateCadena(nombre,"","grammar")
            elif opcion == "4":
                os.system("cls")
            elif opcion.lower() == "salir":
                os.system("cls")
                break
            else:
                os.system("cls")
    else:
        menuMain()
        
def menuArchivo():
    while True:
        print("-----------------Menu Cargar Archivo-------------------")
        print("|                                                     |")
        print("| 1.AFD                                               |")
        print("| 2.Gramatica                                         |")
        print("|   SALIR                                             |")
        print("|                                                     |")
        print("-------------------------------------------------------")
        print("")
        print(">> ",end="")
        opcion = input()
        opcion = opcion.strip()
        if opcion == "1":
            os.system("cls")
            ManejadorArchivo.readArchivo()
        elif opcion == "2":
            os.system("cls")
            ManejadorArchGramar.readArchivo()
        elif opcion.lower() == "salir":
            os.system("cls")
            break
        else:
            os.system("cls")


def menuGuardar():
    nombre = ""
    while True:
        print("-------------------Menu Guadar-------------------------")
        print("|                                                     |")
        print("| 1.El nombre del AFD o Gramatica a guardar           |")
        print("| 2.El nombre con el que desea guardarlo              |")
        print("|   SALIR                                             |")
        print("|                                                     |")
        print("-------------------------------------------------------")
        print("")
        print(">> ",end="")
        opcion = input()
        opcion = opcion.strip()
        if opcion == "1":
            os.system("cls")
            nombre = setNombreGramaticaAFD()
            if ManejadorCadena.existAFDGramatica(nombre) != True:
                 ManejadorCadena.alertaError("No existe el afd o la grammarica")
                 break
        elif opcion == "2":
            os.system("cls")
            if is_empty(nombre.strip()) == False: 
                ManejadorGuardar.transformarArchivo(nombre)
            else:
                ManejadorCadena.alertaError("No ingrese el nombre del AFD o Gramatica")

        elif opcion.lower() == "salir":
            os.system("cls")
            break
        else:
            os.system("cls")
            
            

def is_empty(data_structure):
    if data_structure:
        #print("No está vacía")
        return False
    else:
        #print("Está vacía")
        return True
    
def setNombreGramticaDos():
    print("Ingrese el nombre de la Gramtica Dos")
    print(">> ",end="")
    nombre = input()
    nombre = nombre.strip()
    os.system("cls")
    return nombre 

def setNombreAutomataPila():
    print("Ingrese el nombre para el automata de pila")
    print(">> ",end="")
    nombre = input()
    nombre = nombre.strip()
    os.system("cls")
    return nombre 
    
def menuGramticaTiDos():
    while True:
        print("------------------Gramatica Tipo 2---------------------")
        print("|                                                     |")
        print("| 1.Ingresar/Modificar Gramatica                      |")
        print("| 2.Generar Automata de Pila                          |")
        print("| 3.Visualizar automata                               |")
        print("| 4.Validar Cadena                                    |")
        print("|   SALIR                                             |")
        print("|                                                     |")
        print("-------------------------------------------------------")
        print("")
        print(">> ",end="")
        opcion = input()
        opcion = opcion.strip()
        if opcion == "1":
            os.system("cls")
            menuNuevoGramaticaDos()
        elif opcion == "2":
            os.system("cls")
            nombreGramatica = setNombreGramticaDos()
            nombrePila = setNombreAutomataPila()
            if is_empty(nombreGramatica) == False and is_empty(nombrePila) == False:
                ManejadorAutomaPila.new_automataPila(nombreGramatica,nombrePila)
            else:
                ManejadorAutomaPila.alerta("Datos Vacios")
        elif opcion == "3":
            os.system("cls")
            nombre = setNombreAutomataPila()
            if is_empty(nombre) == False:
                ManejadorAutomaPila.mostrar_sextupla(nombre)
            else:
                ManejadorAutomaPila.alerta("Datos Vacios")
        elif opcion == "4":
            os.system("cls")
            menu_validarCadena()
        elif opcion.lower() == "salir":
            os.system("cls")
            break
        else:
            os.system("cls")
        

def menuNuevoGramaticaDos():
    nombre = setNombreGramticaDos()
    if nombre != "update":
        if ManejadorGramaticaDos.newGramaticaDos(nombre) == True:
            while True:
                print("--------------Menu Gramatica Tipo 2--------------------")
                print("|                                                     |")
                print("| 1.Ingresar Terminales                               |")
                print("| 2.Ingresar No terminales                            |")
                print("| 3.Ingresar No Terminal Inicial                      |")
                print("| 4.Ingresar Producciones                             |")
                print("| 5.Borrar Produccion                                 |")
                print("|   SALIR                                             |")
                print("|                                                     |")
                print("-------------------------------------------------------")
                print("")
                print(">> ",end="")
                opcion = input()
                opcion = opcion.strip()
                if opcion == "1":
                    os.system("cls")
                    ManejadorGramaticaDos.setNewTerminal(nombre)
                elif opcion == "2":
                    os.system("cls")
                    ManejadorGramaticaDos.setNewNoTerminal(nombre)
                elif opcion == "3":
                    os.system("cls")
                    ManejadorGramaticaDos.setNTInicial(nombre)
                elif opcion == "4":
                    os.system("cls")
                    ManejadorGramaticaDos.setProduccion(nombre)
                elif opcion == "5":
                    os.system("cls")
                    ManejadorGramaticaDos.borrar_cadena(nombre)
                elif opcion.lower() == "ver":
                    os.system("cls")
                    ManejadorGramaticaDos.verGramatica(nombre)
                elif opcion.lower() == "salir":
                    os.system("cls")
                    break
                else:
                    os.system("cls")
    elif nombre == "update":
        nombre = setNombreGramticaDos()
        nombre = nombre.strip()
        buscado = ManejadorGramaticaDos.getObjeto(nombre)
        if buscado != None:
            while True:
                print("--------------Menu UPDATE Gramatica Tipo 2-------------")
                print("|                                                     |")
                print("| 1.Ingresar Terminales                               |")
                print("| 2.Ingresar No terminales                            |")
                print("| 3.Ingresar No Terminal Inicial                      |")
                print("| 4.Ingresar Producciones                             |")
                print("| 5.Borrar Produccion                                 |")
                print("|   SALIR                                             |")
                print("|                                                     |")
                print("-------------------------------------------------------")
                print("")
                print(">> ",end="")
                opcion = input()
                opcion = opcion.strip()
                if opcion == "1":
                    os.system("cls")
                    ManejadorGramaticaDos.setNewTerminal(nombre)
                elif opcion == "2":
                    os.system("cls")
                    ManejadorGramaticaDos.setNewNoTerminal(nombre)
                elif opcion == "3":
                    os.system("cls")
                    ManejadorGramaticaDos.setNTInicial(nombre)
                elif opcion == "4":
                    os.system("cls")
                    ManejadorGramaticaDos.setProduccion(nombre)
                elif opcion == "5":
                    os.system("cls")
                    ManejadorGramaticaDos.borrar_cadena(nombre)
                elif opcion.lower() == "ver":
                    os.system("cls")
                    ManejadorGramaticaDos.verGramatica(nombre)
                elif opcion == "salir":
                    os.system("cls")
                    break
                else:
                    os.system("cls")
        else:
            os.system("cls")
            ManejadorGramaticaDos.alerta("No se encontro la Gramtica Tipo 2 :(")
                    
   
def menu_validarCadena():
    nombre = setNombreGramticaDos()
    buscado = ManejadorAutomaPila.search_automataGramatica(nombre.strip())
    if buscado == True:
        while True:
            print("------------------Validar Cadena-----------------------")
            print("|                                                     |")
            print("| 1.Ingresar Cadena                                   |")
            print("| 2.Resultado                                         |")
            print("| 3.Reportes                                          |")
            print("|   SALIR                                             |")
            print("|                                                     |")
            print("-------------------------------------------------------")
            print("")
            print(">> ",end="")
            opcion = input()
            opcion = opcion.strip()
            if opcion == "1":
                os.system("cls")
                ManejadorAutomaPila.validar_Cadena(nombre)
            elif opcion == "2":
                os.system("cls")
            elif opcion == "3":
                os.system("cls")
                ManejadorAutomaPila.get_rutaAutomataPila(nombre)
            elif opcion.lower() == "salir":
                os.system("cls")
                break
            else:
                os.system("cls")
            
    else:
        ManejadorGramaticaDos.alerta("No se encontro la Gramtica Tipo 2 :(")