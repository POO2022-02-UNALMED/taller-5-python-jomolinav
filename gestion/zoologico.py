from zooAnimales.zooAnimales import Animal, Mamifero, Ave, Reptil, Pez, Anfibio

from gestion.zona  import Zona
Tabla = []
class Zoologico:
    
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        zonas= Zona(nombre)
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre
    def getubicacion(self):
        return self.ubicacion
    def setubicacion(self, ubicacion):
        rself.ubicacion = ubicacion
    def getzonas(self):
        return self.zonas
    def setzonas(self, zonas):
        self.zonas = zonas

    
    def agregarZonas(self, zonas):
        Tabla.append(zonas)
    def cantidadTotalAnimales(self,  Total):
        self.Total = Mamifero.cantidadMamiferos + Ave.cantidadAves + Reptil.cantidadReptiles + Pez.cantidadPeces + Anfibio.cantidadAnfibios
