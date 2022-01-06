def enumeracion(numero):
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta**2 == objetivo:
        return f'La raíz cuadrada de {numero} es: {respuesta}'
    else:
        return f'El número {numero} no tiene raíz cuadrada'

print('*****Bienvenido*****')
objetivo = int(input('Ingresa el número del cual quieres obtener la raíz cuadrada: '))
print('*' * 10)
print('1-Enumeración')
print('2-Aproximación')
print('3-Busqueda binaria')

respuesta_usuario = int(input('Selecciona la opción que deseas utilizar para obtener la raíz cuadrada: '))

if respuesta_usuario == 1:
    mensaje = enumeracion(objetivo)
    print(mensaje)