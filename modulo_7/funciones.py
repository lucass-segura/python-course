"""
def <nombre_funcion>(<parámetros, >):
    ...
"""

def count_to(number):
    for n in range(0, number +1):
        print(n)

count_to(10) # Argumento

def full_name(first_name, last_name, age):
    full_name = f' Nombre: {first_name}\n  Apellido: {last_name}\n  Edad: {age}'
    return full_name

data = full_name('Agustin', 'Segura', 22)
print(f'\nLos datos del usuario son:\n {data}\n')