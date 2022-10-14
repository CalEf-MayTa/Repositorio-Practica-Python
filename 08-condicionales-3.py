#Ejemplo de multiples condiciones
#Operadores and y or

usuario_loguado = False
usuario_admin = False

#ejemplo con AND
if usuario_loguado and usuario_admin:
    #se ejecuta solo si ambas condiciones
    #son verdaderas
    print('Acceso de Administrador')
    #si no se cumple almenos una pasara
elif usuario_loguado:
    #se ejecuta solo si usuario_loguado se cumple
    print('Acceso al Sistema')
else:
    print('Debes Iniciar Sesion')

#ejemplo con OR
if usuario_loguado or usuario_admin:
    #se ejecuta si almenos una condicion sea verdadera
    print('Acceso de Administrador')
    #si no se cumple almenos una pasara
elif usuario_loguado:
    #se ejectara si ambas condiciones son falsas
    print('Acceso al Sistema')
else:
    print('Debes Iniciar Sesion')
