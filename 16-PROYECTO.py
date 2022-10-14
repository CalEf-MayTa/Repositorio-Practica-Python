from ast import Expression, Try
import os
from re import I
from symbol import try_stmt
from time import process_time_ns

CARPETA = 'contactos/' # Carpeta de Contactos
EXTENCION = '.txt' # Extencion de archivos

class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    
    # Revisar si la existe o no
    crear_directorio()

    #Muestra del menu de opciones
    mostrar_menu() #llamando a la funcion mostrar_menu

    # Preguntar al usuario la accion a realizar
    preguntar = True
    while preguntar:
        opcion = input('Selecciones una opcion: \r\n')
        opcion = int(opcion)

        #Ejecutar las opciones
        if opcion == 1:
            #print('Agregar contacto')
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            #print('Editar contacto')
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            #print('Ver contactos')
            preguntar = False
        elif opcion == 4:
            #print('Buscar contacto')
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            print('Eliminar contacto')
            eliminar_contacto()
            preguntar = False
        else:
            print('Opcion no valida...')
            print('Intente de nuevo')

def eliminar_contacto():
    #Provando la funcion eliminar_contacto()
    #print('Desde eliminar_contacto() ... ')

    nombre = input('Seleccione el Contacto que desea eliminar: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENCION)
        print('\r\n Eliminado Correctamente ')
    except Expression as identifier:
        print('No existe ese contacto')

    app()

def buscar_contacto():
    #prueva de funcion buscar contacto
    #print('Desde buscar_contacto()... ')

    nombre = input('Selecciones el Contacto que desea buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENCION) as contacto:
            print('\r\n Informacion del Contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe ... ')
        print(IOError)

    #reiniciando la app()
    app()

def mostrar_contactos():
    #Prueva de mostrar contactos
    #print('Desde mostrar_contactos()')
    archivos = os.listdir(CARPETA)

    #validado de que el archivo termine en la extencion asignada .txt
    archivos_txt = [i for i in archivos if i.endswith(EXTENCION)]

    #recorriendo los archivos
    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                #Imprime los contenidos
                print(linea.rsplit())
            #Imprime un separador entre contactos
            print('\r\n')
    
    #reiniciamos la app()
    app()

def editar_contacto():
    print('Escribe el Nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')

    #revisar si el archivo existe antes de editarlo
    existe = existe_contacto(nombre_anterior)

    #si existe pasaremos a editar
    if existe:
        #Provando si existe para editar
        #print('Puedes editar')
        with open(CARPETA + nombre_anterior + EXTENCION, 'w') as archivo:

            #Resto de los campos
            nombre_contacto = input('Agrega el Nuevo Nombre: \r\n')
            telefono_contacto = input('Agrega el Nuevo Teléfono: \r\n')
            categoria_contacto = input('Agrega la Nueva Categoría: \r\n')

            #Instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            #Renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENCION, CARPETA + nombre_contacto + EXTENCION)

            #Mostrar un mensaje de exito
            print('\r\n Contacto Editado Correctamente \r\n')

    else:
        print('Ese Contacto no existe')
    
    #Reiniciar la aplicacion
    app()

#Definimos la C de crear contacto como
#   una funcion agregar contacto
def agregar_contacto():
    #Prueva de agragar contacto
    print('Escribe los datos para agragar el nuevo contacto...')
    nombre_contacto = input('Nombre del contacto: \r\n')

    #Revisar si el archivo esiste antes de crearlo
    existe = existe_contacto(nombre_contacto)

    #validamos con un if
    #si no existe pasaremos crearlo
    if not existe:

        #Abrimos y agragamos un archivo de texto 
        #se reliza un concatenado de CARPETA, nombre de contacto a agragar y EXTENCION del archivo
        with open(CARPETA + nombre_contacto + EXTENCION, 'w') as archivo:

            #Resto de los campos
            telefono_contacto = input('Agregar el telefono:\r\n')
            categoria_contacto = input('Categoria Contacto:\r\n')

            #Instanciar la clase Contacto
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #llamar al archivo y escribir con el permiso con w
            archivo.write('Nombre: '+ nombre_contacto + '\r\n')
            archivo.write('Teléfono: '+ telefono_contacto + '\r\n')
            archivo.write('Categoria: '+ categoria_contacto + '\r\n')

            #Mostramos un abiso de exito de guardado de contacto
            print('\r\n Contacto Creado Correctamente \r\n')
    else:
        print(nombre_contacto + ' ya existe en los CONTACTOS')

    #Reiniciando la app
    app()

def mostrar_menu():
    print('Seleccione del Menú lo que desea hacer:')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')

def crear_directorio():
    if not os.path.exists(CARPETA):
        # crear la carpeta
        os.makedirs(CARPETA)
    #else:
        #print('La carpeta ya existe...')

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENCION)

app()