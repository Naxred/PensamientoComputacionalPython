def enumeracion(numero):
    respuesta = 0

    while respuesta**2 < numero:
        respuesta += 1

    if respuesta**2 == numero:
        return f'La raíz cuadrada de {numero} es: {respuesta}'
    else:
        return f'El número {numero} no tiene raíz cuadrada'

def aproximacion(numero):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - numero) >= epsilon and respuesta <= numero:
        respuesta += paso
    
    if abs(respuesta**2 - numero) >= epsilon:
        return f'El número {numero} no tiene raíz cuadrada'
    else:
        return f'La raíz cuadrada de {numero} es: {respuesta}'

def busqueda_binaria(numero):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - numero) >= epsilon:
        if respuesta**2 < numero:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2
    return f'La raíz cuadrada de {numero} es: {respuesta}'



print('*****Bienvenido*****')
print('Primero escoge el número del cual quieres obtener la raíz cuadrada')
objetivo = int(input())
print('*' * 10)
print('Ahora selecciona el método por el cual deseas obtener la raíz cuadrada')
print('Toma en cuenta que el método 1 y 2 solamente dan raíces exactas y el tercero lo puede dar con decimales')
print('1-Enumeración')
print('2-Aproximación')
print('3-Busqueda binaria')

respuesta_usuario = int(input('Selecciona la opción que deseas utilizar para obtener la raíz cuadrada: '))

if respuesta_usuario == 1:
    print(enumeracion(objetivo))

elif respuesta_usuario == 2:
    print(aproximacion(objetivo))

elif respuesta_usuario == 3:
    print(busqueda_binaria(objetivo))

else: 
    print('No se registro una respuesta valida')