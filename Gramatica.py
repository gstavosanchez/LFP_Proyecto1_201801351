class Gramatica():
    nombre =""
    noTerminal = []
    terminal = []
    inicio = ""
    produccion = {}
    transformada = []
    estadosAceptacion = []
    cadenas = []
    cadenasValidas = []
    cadenasNoValidas = [] 

    def __init__(self,nombre,noTerminal,terminal,inicio,produccion,transformada,estadosAceptacion,cadenas,cadenasValidas,cadenasNoValidas):
        self.nombre = nombre
        self.noTerminal = noTerminal
        self.terminal = terminal
        self.inicio = inicio
        self.produccion = produccion
        self.transformada = transformada
        self.estadosAceptacion = estadosAceptacion
        self.cadenas = cadenas
        self.cadenasValidas = cadenasValidas
        self.cadenasNoValidas = cadenasNoValidas


    def getCadena(self):
        return self.cadenas
    def setCadena(self,cadenas):
        self.cadenas = cadenas
    
    def getCadenaValida(self):
        return self.cadenasValidas        
    def setCadenaValida(self,cadenasValidas):
        self.cadenasValidas = cadenasValidas
        
    def getCadenaNoValida(self):
        return self.cadenasNoValidas
    def setCadenaNoValida(self,cadenasNoValidas):
        self.cadenasNoValidas = cadenasNoValidas
    
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre = nombre
    
    def getNoTerminal(self):
        return self.noTerminal
    def setNoTerminal(self,noTerminal):
        self.noTerminal = noTerminal
    
    def getTerminal(self):
        return self.terminal
    def setTerminal(self,terminal):
        self.terminal = terminal
    
    def getInicio(self):
        return self.inicio
    def setInicio(self,inicio):
        self.inicio = inicio
    
    def getProduccion(self):
        return self.produccion
    def setProduccion(self,produccion):
        self.produccion = produccion
    
    def getTransformada(self):
        return self.transformada
    def setTransformada(self,transformada):
        self.transformada = transformada
        
    def getEstadosAceptacion(self):
        return self.estadosAceptacion
    def setEstadosAceptacion(self,estadosAceptacion):
        self.estadosAceptacion = estadosAceptacion