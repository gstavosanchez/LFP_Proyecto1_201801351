class GramaticaDos():
    nombre = ""
    noTerminal = []
    terminal = []
    noTerminalInicial = ""
    produccion = {}
    proTransformada = {}
    
    
    def __init__(self,nombre,noTerminal,terminal,noTerminalInicial,produccion,proTransformada):
        self.nombre = nombre
        self.noTerminal = noTerminal
        self.terminal = terminal
        self.noTerminalInicial = noTerminalInicial
        self.produccion = produccion
        self.proTransformada = proTransformada
        
    
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
    
    def getNoTerminalInicial(self):
        return self.noTerminalInicial
    def setNoTerminalIncial(self,noTerminalInicial):
        self.noTerminalInicial = noTerminalInicial
        
    def getProduccion(self):
        return self.produccion
    def setProduccion(self,produccion):
        self.produccion = produccion
    
    def getProTransformada(self):
        return self.proTransformada
    def setProTransformada(self,proTransformada):
        self.proTransformada = proTransformada

        
        

        
    
    
