class Restaurant:

    def __init__(self, nombre, categoria, precio):
        # Atributos

        self.nombre = nombre #public default: Public, PROTECTED
        self.categoria = categoria
        # un solo guion bajo le hace un atributo protegido "PROTECTED"
        # dos guion bajo le hace un atributo privado "PRIVATE"
        self.__precio = precio

        #prueva de funcionamiento
        #print('Yo me ejecuto automaticamente')

    def mostrar_informacion (self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}')
    
    # GETTERS Y SETTERS - GET = Obtiene un valor, SET = Agrega un valor
    # para acceder es recomendable nombrar u atributo como get_"atributo"
    def get_precio(self):
        #print(self.__precio)
        return self.__precio
    
    def set__precio(self, precio):
        self.__precio = precio

    #Anterior forma de los metodos:
    #def agregar_restaurant(self, nombre):
        #self.nombre = nombre #Atributo

    #def nostrar_informacion(self):
        #print(f'Nombre: {self.nombre}')

#Instanciar la clase
restaurant = Restaurant('Pizzeria Mexico', 'Comida Italiana', 50)
#   a este print no podra acceder al atributo __precio
#print(restaurant.__precio)
# se raliza un encapsulamiento con un valor determinado
# que no se pueda modificar
#restaurant.__precio = 80 #no sera posible modificar con PRIVATE __
restaurant.mostrar_informacion()
restaurant.set__precio(80)
precio = restaurant.get_precio()
print(precio)

restaurant2 = Restaurant('Hamburgesas Python', 'Comida Casual', 20)
#print(restaurant2.__precio)
#restaurant2.__precio = 40
restaurant2.mostrar_informacion()
restaurant2.set__precio(40)
restaurant2.get_precio()

