class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Atributo
        self.categoria = categoria
        self.precio = precio
        #prueva de funcionamiento
        #print('Yo me ejecuto automaticamente')

    def mostrar_informacion (self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')

    #Anterior forma de los metodos:
    #def agregar_restaurant(self, nombre):
        #self.nombre = nombre #Atributo

    #def nostrar_informacion(self):
        #print(f'Nombre: {self.nombre}')

#Instanciar la clase
restaurant = Restaurant('Pizzeria Mexico', 'Comida Italiana', 50)
restaurant.mostrar_informacion()

restaurant2 = Restaurant('Hamburgesas Python', 'Comida Casual', 20)
restaurant2.mostrar_informacion()