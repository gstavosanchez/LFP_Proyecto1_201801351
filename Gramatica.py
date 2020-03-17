class Gramatica():
    nombre =""
    noTerminal = []
    terminal = []
    inicio = ""
    produccion = {}
    transformada = []

    def __init__(self,nombre,noTerminal,terminal,inicio,produccion,transformada):
        self.nombre = nombre
        self.noTerminal = noTerminal
        self.terminal = terminal
        self.inicio = inicio
        self.produccion = produccion
        self.transformada = transformada

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