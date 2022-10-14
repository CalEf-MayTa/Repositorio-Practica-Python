pregunta = 'Agregar un numero y te dire si es par o impar \r\n'
pregunta += ' (Escribe "cerrar" para salir de la aplicación ) \r\n'
preguntar = True

while preguntar:

    #Mesclador con operadores
    numero = input(pregunta)

    if numero == 'cerrar':
        preguntar = False
    else:
        numero = int(numero)
        #para saber el residuo
        #para podemos saber si es par o inpar

        if numero % 2 == 0:
            print(f'El numero {numero} es par')
        else:
            print(f'El numero {numero} es impar')

