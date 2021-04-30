class Restaurante:
    #constructor
    def __init__ (self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.__precioMedio = precio  #privada
        print(f"Agregando restaurante: {self.nombre}, de categoria: {self.categoria} ")

    def getPrecioMedio(self):
        return self.__precioMedio
    
    def setPrecioMedio(self, precio):
        self.__precioMedio = precio

    """
    def agregarRestaurante(self, nombre):
        self.nombre = nombre
        print(f"Agregando restaurante: {self.nombre}")
     """

#creo la instancia Restaurante
restaurante = Restaurante("Pizzeria Vegan", "Comida vegana",400)
print("El precio medio del restaurante es:"+str(restaurante.getPrecioMedio()))
restaurante.setPrecioMedio(500)
print("El precio medio AHORA del restaurante es:"+str(restaurante.getPrecioMedio()))
#restaurante.agregarRestaurante("Pizzeria vegan")

class Hotel(Restaurante):
    def __init__(self, nombre, categoria, precio, alberca):
        super().__init__(nombre, categoria, precio)
        self.alberca = alberca
    
    def getAlberca(self):
        return self.alberca

hotel = Hotel("Hotel POO","5 estrellas",300, "Si")