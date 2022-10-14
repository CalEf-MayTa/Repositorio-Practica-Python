playlist = {} #Diccionario vacio
playlist['canciones'] = [] #lista vacio de canciones

#Funcion principal
def app():
    #Agregar playlist
    agregar_playlist = True

    #se incorporara en un bucle para nombrar la playlist

    while agregar_playlist:
        nombre_playlist = input('¿Como desea nombrar la playlist? \r\n')

        if nombre_playlist:
            playlist['nombre'] = nombre_playlist

            # Al tener un nombre de la playlist
            # desactivar el True de agregar_playlist
            agregar_playlist = False
            #provando del nombramiento
            #print( playlist )

            #Mandar a llamar a la funcion para agregar canciones
            agregar_canciones()

def agregar_canciones():
        #print('Agregar canciones...')
    #Bandera para agregar canciones
    agregar_canciones = True
    
    while agregar_canciones:
        #Preguntar al usuario que canciones desea agregar
        nombre_playlist = playlist['nombre']
        pregunta = f'\r\nAgrega canciones para la playlist {nombre_playlist}: \r\n'
        pregunta += 'Escribe "X" para dejar de agregar canciones: \r\n'

        cancion = input(pregunta)

        if cancion == 'X':
            #Dejar de agregar canciones
            #probando el funcionamiento:
            #print('finalizado...')

            #Dejar de agregar canciones
            agregar_canciones = False

            #Mostrar resumen de la playlist
            mostrar_resumen()


        else:
            #Agregar las conciones a la playlist
            playlist['canciones'].append(cancion)

            #probando el funcionamiento:
            #print(playlist)

def mostrar_resumen():
    #para mostrar si hay comunicacion
    #print('Mostrar resumen...')
    nombre_playlist = playlist['nombre']
    print(f'Playlist: {nombre_playlist} \r\n')
    print('Canciones: \r\n')
    for cancion in playlist['canciones']:
        print(cancion)

app()

#tips para el funcionamiento
#1-Dividir las tareas por secciones
#2-probar con un print cada paso o sierta cantidad de lineas
#3-delinear cada comanado y sub comando