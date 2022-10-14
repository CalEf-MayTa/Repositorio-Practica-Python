def app():
    
    # r es lectura, pero no es necesario
    #   porque por defecto se inicia con lectura
    with open('archivo.txt') as archivo: 
        for contenido in archivo:
            print(contenido.rstrip())
    
app()