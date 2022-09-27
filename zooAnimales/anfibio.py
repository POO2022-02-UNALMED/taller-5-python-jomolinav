from zooAnimales.animal import Animal

class Anfibio(Animal):

    def __init__(self, listado, ranas, salamandras, colorPiel, venenoso):
        self.listado = Anfibio
        self.ranas = ranas
        self.salamandras = salamandras
        self.colorPiel = colorPiel
        self.venenoso = venenoso
    def getlistado(self):
        return self.listado
    def setlistado(self, listado):
        self.listado = listado
    def getcolorPiel(self):
        return self.colorPiel
    def setcolorPiel(self, colorPiel):
        self.colorPiel = colorPiel
    def setvenenoso(self):
        return self.venenoso
    def getvenenoso(self, venenoso):
        self.venenoso = venenoso


    def cantidadAnfibios(self, totalanf):
        totalanf = self.ranas + self.salamandras
    def movimiento(self):
        None
    def crearRana(nombre, edad, genero):
        
        habitat = "selva"
        colorPiel = "rojo"
        venenoso = True
    def crearSalamandra(nombre, edad, genero):
        
        habitat = "selva"
        colorPiel = "negro y amarillo"
        venenoso = False


   
   