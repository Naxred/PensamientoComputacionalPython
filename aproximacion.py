objetivo = int(input('Escoge un número: '))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0
print('Aqui empieza el ciclo**')
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo))
    print(f'la respuesta va en: {respuesta}')
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raíz cuadrada de {objetivo}')
else:
    print(f'La raíz cuadrada del {objetivo} es {respuesta}')
    