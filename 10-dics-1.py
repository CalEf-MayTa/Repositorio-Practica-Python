# Creando un diccionario simple

cancion = {
    'Artista' : 'Metallica', #llave y valor
    'cancion' : 'Enter Sandman',
    'lanzamiento' : 1992,
    'likes' : 3000
}

#Acceder a los elementos del diccionario
print(cancion)
print(cancion['Artista']) #Accedemos al elemento Artista
print(cancion['lanzamiento']) #Accedemos a la fecha de lanzamiento

#Mezclar con un string
artista = cancion['Artista']
print(f'Estoy escuchando a {artista}')

#agregar nuevos valores
cancion['playlist'] = 'Heavy Metal'
print(cancion)

#Reemplazar valor existente
cancion['cancion'] = 'Seek & Destroy'
print(cancion)

#Eliminar un valor
del cancion['lanzamiento']
print(cancion)
