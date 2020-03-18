class AFD():
    nombre = ""
    estado = []
    alfabeto =[]
    estadoInicial = ""
    estadosAceptacion = []
    trancisiones = {}

    def __init__(self,nombre,estado,alfabeto,estadoInicial,estadosAceptacion,trancisiones):
        self.nombre = nombre
        self.estado = estado
        self.alfabeto = alfabeto
        self.estadoInicial = estadoInicial
        self.estadosAceptacion = estadosAceptacion
        self.trancisiones = trancisiones
    
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
         
    
    