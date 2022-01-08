def factorial(n):
    """Calcula el factorial de n.
    n int > 0
    returns n!
    """
    if n == 1:
        return 1
    
    return n * factorial(n-1)

numero = int(input('Escoge un numero: '))

print(factorial(numero))