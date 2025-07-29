# A(B) -> C
# A (Decorador)
# B (Función a decorar (Base))
# C (Funcion decorada Base + Nuevas líneas de código)

              # B
def decorator(func): # A

    def wrapper(*args, **kwargs): # C
        print('>>> Comenzamos la operación...')
        func(*args, **kwargs)
        print('>>> Fin de la operación...')

    return wrapper

@decorator
def hello_world():
    print('Hello world!')

@decorator
def suma(n1, n2):
    print(n1 + n2)

hello_world()
suma(10,20)