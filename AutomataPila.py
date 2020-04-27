class AutomataPila():
    nombre = ""
    simbolosDePila = []
    estado = []
    alfabeto = []
    estadoInicial = ""
    estadosAceptacion = ""
    trancisiones = {}
    pila = []
    imagen = ""
    
    def __init__(self,nombre,estado,alfabeto,estadoInicial,estadosAceptacion,trancisiones,simbolosDePila,pila,imagen):
        self.nombre = nombre
        self.estado = estado
        self.alfabeto = alfabeto
        self.estadoInicial = estadoInicial
        self.estadosAceptacion = estadosAceptacion
        self.trancisiones = trancisiones
        self.simbolosDePila = simbolosDePila
        self.pila = pila
        self.imagen = imagen

    def getImagen(self):
        return self.imagen
    def setImagen(self,imagen):
        self.imagen = imagen
     
    def getPila(self):
        return self.pila
    def setPila(self,pila):
        self.pila = pila
    
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre = nombre
     
    def getSimboloDePila(self):
        return self.simbolosDePila 
    def setSimboloDePila(self,simbolosDePila):
        self.simbolosDePila = simbolosDePila
    
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