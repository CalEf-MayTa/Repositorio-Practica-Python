#creacion de la funcion
#entre parentesis es el parametro
#ademas parametro por defecto en comilla simple
def informacion(nombre, puesto = 'Desconocido'):
    #acciones de la funcion
    #siempre dentro de un tab
    print(f'Soy {nombre} y soy {puesto}')

#podemos repetir la funcion cuantas veces se requiera
#agregamos argumentos a la funcion creada mediante 
#comillas simples
informacion('Pedro', 'Programador')
informacion('Itzel', 'Diseñadora')
#al no haber informacion de parametro
#se reescribe el parametro por defecto
#que se encuentra entre comillas
informacion('Juan')
