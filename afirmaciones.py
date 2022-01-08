def primera_letra(lista_de_palabras):

    primeras_letras = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es un string'
        assert len(palabra) > 0, f'No se permiten strings vacios'

        primeras_letras.append(palabra[0])
    
    return primeras_letras

palabras = ['Isaac', 'Reyna', 'Uresti', '']

print(primera_letra(palabras))