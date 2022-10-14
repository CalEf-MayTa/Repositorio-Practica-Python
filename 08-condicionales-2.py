#Ejemplo con elif
#dependiendo de la acupacion tendra un descuento
ocupacion = 'Desempleado'

if ocupacion == 'Estudiante':
	print('Tienes 50% de Descuento')
elif ocupacion == 'Jubilado':
	print('Tienes el 75% de Descuento')
elif ocupacion == 'Desempleado':
    print('Tienes un 10% de Descuento')
else:
	print('Debes pagar el 100%')