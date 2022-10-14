#Al crear una clase la primera letra del nombre de la clase a de ser Mayuscula

class Restaurant:
    #Cuerpo de la clase
    def agregar_restaurant(self, nombre):
        #probando si llama al metodo
        #print('Agregando...')
        self.nombre = nombre #Atributo
    def mostrar_informacion(self):
        print(f'Nombre {self.nombre}')

#Intanciar la clase es como llamar a la clase
#   mediante una variable que creemos
restaurant = Restaurant() # Nombre de la variable que elijas = Nombre de la clase con ()

# probando la obtencion de datos por la clase
#print(restaurant)

# llamando a la funcion que esta dentro de la clase
#   llamado metodo:
# self se intecgra automaticamente
restaurant.agregar_restaurant('Pizzeria Mexico')
restaurant.mostrar_informacion()

restaurant2 = Restaurant()
restaurant2.agregar_restaurant('Hamburgesas Python')
restaurant2.mostrar_informacion()

#Mostrar la informacion
print(f'Nombre Restaurant: {restaurant.nombre}')
print(f'Nombre Restaurant: {restaurant2.nombre}')