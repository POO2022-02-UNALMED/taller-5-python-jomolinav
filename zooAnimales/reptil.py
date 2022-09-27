from zooAnimales.animal import Animal

class Reptil(Animal):
    def __init__(self, listado, iguanas, serpientes, colorEscamas, largoCola):
        self.listado = Reptil
        self.iguanas = iguanas
        self.serpientes = serpientes
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola

    def getlistado(self):
        return self.listado
    def setlistado(self, listado):
        self.listado = listado
    def getlargoCola(self):
        return self.largoCola
    def setlargoCola(self, largoCola):
        self.largoCola = largoCola
    def getcolorEscamas(self):
        return self.colorEscamas
    def setcolorEscamas(self, colorEscamas):
        self.colorEscamas = colorEscamas

    def cantidadReptiles(self, totalrep):
        totalrep = self.serpientes + self.iguanas
        return totalrep
    def movimiento(self):
        None
    def crearIguana(nombre, edad, genero):
        
        
        colorEscamas = "verde"
        largoCola = 3
        habitat = "humedal"

    def crearSerpiente(nombre, edad, genero):
        
        habitat = "jungla"
        colorEscamas = "blanco"
        largoCola = 1