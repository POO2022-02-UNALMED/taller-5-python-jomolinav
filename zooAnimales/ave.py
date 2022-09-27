from zooAnimales.animal import Animal

class Ave(Animal):
    def __init__(self, listado, halcones, aguilas, colorPlumas):
        
        self.listado = Ave
        self.halcones = halcones
        self.aguilas = aguilas
        self.colorPlumas = colorPlumas
        listado = []
    def getlistado(self):
        return self.listado
    def setlistado(self, listado):
        self.listado = listado
    def getcolorPlumas(self):
        return self.colorPlumas
    def setcolorPlumas(self, colorPlumas):
        self.colorPlumas = colorPlumas
    

    def cantidadAves(self, totalave):
        totalave = self.aguilas + self.halcones
        return totalave
    def movimiento(self):
        None 
    def crearHalcon(nombre, edad, genero):
 
        colorPlumas = "Cafe Glorioso"
        habitat = "montanas"

    def crearAguila(nombre, edad, genero):

        habitat = "montanas"
        colorPlumas = "blanco y amarillo"
