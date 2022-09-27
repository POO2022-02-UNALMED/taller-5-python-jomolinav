from zooAnimales.animal import Animal

class Pez(Animal):

    def __init__(self, listado, salmones, bacalaos, colorEscamas, cantidadAletas):
        self.listado = Pez
        self.salmones = salmones
        self.bacalaos = bacalaos
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas
    
    def getlistado(self):
        return self.listado
    def setlistado(self, listado):
        self.listado = listado
    def getcolorEscamas(self):
        return self.colorEscamas
    def setcolorEscamas(self, colorEscamas):
        self.colorEscamas = colorEscamas
    def getcantidadAletas(self):
        return self.cantidadAletas
    def setcantidadAletas(self, cantidadAletas):    
        self.cantidadAletas = cantidadAletas

    def cantidadPeces(self, totalPec):
        totalPec = self.salmones + self.bacalaos
        return totalPec
    def movimiento(self):
        None
    def crearSalmon(nombre, edad, genero):
       
       habitat = "oceano"
       colorEscamas = "rojo"
       cantidadAletas = 6

    def crearBacalao(nombre, edad, genero):
    
        habitat = "oceano"
        colorEscamas = "gris"
        cantidadAletas = 6