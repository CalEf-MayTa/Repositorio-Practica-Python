class Restaurant:

    def __init__(self, nombre, categoria, precio):
        #Atributos
        self.nombre = nombre
        self.categoria = categoria
        self.__precio = precio

    def mostrar_informacion (self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}')
    
    # GETTERS Y SETTERS - Get = Obtiene un valor, Set = Agrega un valor
    def get_precio(self):
        #print(self.__precio)
        return self.__precio
    
    def set__precio(self, precio):
        self.__precio = precio

#           HERENCIA
#Crear una clase hijo de Restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio)

hotel = Hotel('Hotel POO', '5 Estrellas', 200)
hotel.mostrar_informacion()
