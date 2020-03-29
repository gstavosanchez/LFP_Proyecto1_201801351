class AFD():
    nombre = ""
    estado = []
    alfabeto =[]
    estadoInicial = ""
    estadosAceptacion = []
    trancisiones = {}
    cadenas = []
    cadenasValidas = []
    cadenasNoValidas = []

    def __init__(self,nombre,estado,alfabeto,estadoInicial,estadosAceptacion,trancisiones,cadenas,cadenasValidas,cadenasNoValidas):
        self.nombre = nombre
        self.estado = estado
        self.alfabeto = alfabeto
        self.estadoInicial = estadoInicial
        self.estadosAceptacion = estadosAceptacion
        self.trancisiones = trancisiones
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
    
    def getEstado(self):
        return self.estado
    def setEstado(self,estado):
        self.estado = estado
    
    def getAlfabeto(self):
        return self.alfabeto
    def setAlfabeto(self,alfabeto):
        self.alfabeto = alfabeto

    def getEstadoInicial(self):
        return self.estadoInicial
    def setEstadoInicial(self,estadoInicial):
        self.estadoInicial = estadoInicial
    
    def getEstadosDeAceptacion(self):
        return self.estadosAceptacion
    def setEstadosDeAceptacion(self,estadosAceptacion):
        self.estadosAceptacion = estadosAceptacion
    
    def getTrancisiones(self):
        return self.trancisiones
    def setTrancisiones(self,trancisiones):
        self.trancisiones = trancisiones
         
    
    