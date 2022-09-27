class Animal:
    def __init__(self, totalAnimales, nombre, edad, habitat, genero, zona):
        self.totalAnimales = totalAnimales
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.zona = Zona
        self.totalAnimales = cantidadMamiferos + cantidadAnfibios + cantidadAves + cantidadPeces + cantidadReptiles
    def gettotalAnimales(self):
        return self.totalAnimales
    def settotalAnimales(self, totalAnimales):
        self.totalAnimales = totalAnimales
    def getnombre(self):
        return self.nombre
    def setnombre(self, nombre):
        self.nombre = nombre
    def getedad(self):
        return self.edad
    def setedad(self, edad):
        self.edad = edad
    def gethabitat(self):
        return self.habitat
    def sethabitat(self, habitat):
        self.habitat = habitat
    def getgenero(self):
        return self.genero
    def setgenero(self, genero):
        self.genero = genero
    def getzona(self):
        return self.zona
    def setzona(self, zona):
        self.zona = zona
    
    
    
    
    def movimiento(self):
        None
    def totalPorTipo(self):
        return ("Mamiferos", cantidadMamiferos, "Aves", cantidadAves, "Reptiles", cantidadReptiles, "Peces", cantidadPeces, "Anfibios", cantidadAnfibios, totalAnimales , "es el numero de animales por cada subclase")

    def toString(self):
        return ("Mi nombre es" , self.nombre, "tengo una edad de" , self.edad, "habito en", self.habitat , "y mi genero es", self.genero, "la zona en la que me ubico es" , self.zona, "en el", self.zoo)
      
    