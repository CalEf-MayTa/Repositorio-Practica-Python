#Entrada de datos por el usuario
nombre = input('Cuál es tu nombre: \r\n')

print(f'Hola {nombre}')

#leer datos que seran numeros
edad = input('Cual es tu edad?')
#convertir edad (string) a int
edad = int(edad)

if edad >= 18:
    print('Ya puedes votar')
else:
    print('Aún no puedes votar')
#La entrada de datos siempre es un string

#Mesclador con operadores
numero = input('Agrega un numero y te dire si es par o no \r\n')

numero = int(numero)
#para saber el residuo
#para podemos saber si es par o inpar
print(numero % 2)

if numero % 2 == 0:
    print(f'El numero {numero} es par')
else:
    print(f'El numero {numero} es impar')



