#Revisar si una condiciona es mayor a 
balance = 500
if balance > 0:
    print('Puedes pagar')
else:
    print('No tiene saldo')

#Likes
likes = 200
if likes >= 200:
    print('Excelente, 200 likes')
else:
    print('Casi llegas a los 200')

#IF con texto
lenguaje ='PHP'
#if not te lleva al valor contrario
if not lenguaje == 'Python':
    #al negar el if evaluamos
    #lo que sea diferente a
    #       'texto o variable'
    print('Excelente decisión')

#Evauar un Boolean
usuario_autenticado = True

#evalua si la condicion es verdades
if usuario_autenticado: # es lo mismo que poner
                        # == True
    print('Acceso al sistema')
else:
    print('Debes iniciar sesión')

#Evaluar si un elemento esta en la lista
lenguajes = [ 'Python', 'Klotin', 'Java', 'JavaDcript', 'PHP', 'Ruby', 'GO'];
if 'PHP' in lenguaje:
    print('PHP Si existe')
else:
    print('No esta en la lista')

#   if anidados
usuario_autenticado = True
usuario_admin = True
if usuario_autenticado:
    # se identifica si la condicion es vedadera
    if usuario_admin:
        #se identifica si la condicion es verdadera
        #si usuario_autenticado y usuario_admin son vedaderas
        print('ACCESO TOTAL')
    else:
        #solo si usuario_autenticado es vedadera
        print('Acceso al sistema')
else:
    #si ninguna es vedadera o solo usuario_admin
    print('Debes iniciar sesión')
