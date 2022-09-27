from zooAnimales.animal import Animal

class Mamifero(Animal):
    def __init__(self, listado, caballos, leones, pelaje, patas):
        self.listado = Mamifero

        self.caballos = caballos
        self.leones = leones
        self.pelaje = pelaje
        self.patas = patas 
    

    def getlistado(self):
        return self.listado
    def setlistado(self, listado):
        self.listado = listado
    def getpelaje(self):
        return self.pelaje
    def setpelaje(self, pelaje):
        self.pelaje = pelaje
    def getpatas(self):
        return self.patas
    def setpatas(self, patas):
        self.patas = patas



    def cantidadMamiferos(self, totalmami):
        totalmami = self.leones + self.caballos 
        return totalmami
    def crearCaballo(nombre, edad, genero):
        pelaje = True
        patas = 4
        habitat = "pradera"
    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        
        pelaje = True
        habitat = "Selva"
        patas = 4
