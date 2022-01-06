nombre_usuario1 = input('Ingresa el nombre de la primer persona: ')
nombre_usuario2 = input('Ingresa el nombre de la segunda persona: ')

edad_usuario1 = int(input(f'Ingresa la edad de {nombre_usuario1}: '))
edad_usuario2 = int(input(f'Ingresa la edad de {nombre_usuario2}: '))

if edad_usuario1 > edad_usuario2:
    print(f'{nombre_usuario1} es mayor que {nombre_usuario2}')
elif edad_usuario2 > edad_usuario1:
    print(f'{nombre_usuario2} es mayor que {nombre_usuario1}')
else:
    print('Ambas personas tienen la misma edad')
