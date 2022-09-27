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
    def crearCaballos(self):
        c = Mamifero()
        c.pelaje = True
        c.patas = 4
        c.habitat = "pradera"
        self.caballos = self.caballos+1
    def crearLeon():
        leo = Mamifero()
        leo.pelaje = True
        leo.habitat = "Selva"
        leo.patas = 4
        self.leones = self.leones
    
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
    def crearHalcon(self):
        hal = Ave()
        hal.colorPlumas = "Cafe Glorioso"
        hal.habitat = "montanas"
        self.halcones = self.halcones + 1
    def crearAguila(self):
        agu = Ave()
        agu.habitat = "montanas"
        agu.colorPlumas = "blanco y amarillo"
        self.aguilas = self.aguilas + 1
    
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
    def crearIguana(self):
        self. iguanas = self.iguanas + 1 
        ig = Reptil()
        ig.colorEscamas = "verde"
        ig.largoCola = 3
        ig.habitat = "humedal"

    def crearSerpiente(self):
        self.serpientes = self.serpientes + 1
        ser = Reptil()
        ser.habitat = "jungla"
        ser.colorEscamas = "blanco"
        ser.largoCola = 1

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
    def crearSalmon(self, salm):
       self.salmones = self.salmones+1
       salm = Pez()

       salm.habitat = "oceano"
       salm.colorEscamas = "rojo"
       salm.cantidadAletas = 6

    def crearBacalao(self, baca):
        self.bacalaos = self.bacalaos+1
        baca = Pez()
        baca.habitat = "oceano"
        baca.colorEscamas = "gris"
        baca.cantidadAletas = 6
    
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
    def crearRana(self, ran):
        self.ranas = self.ranas + 1
        ran = Anfibio()
        ran.habitat = "selva"
        ran.colorPiel = "rojo"
        ran.venenoso = True
    def crearSalamandra(self, mandra):
        self.salamandras = self.salamandras + 1
        mandra = Anfibio()
        mandra.habitat = "selva"
        mandra.colorPiel = "negro y amarillo"
        mandra.venenoso = False


   
    