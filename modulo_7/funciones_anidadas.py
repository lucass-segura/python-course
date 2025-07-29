def outer_function():
    message = 'Hola'

    def iner_function():
        nonlocal message # Sirve para acceder a una variable local de una funcion exterior y poder modificarla
        message = 'Hola Mundo!'
    
    iner_function()
    print(message)

outer_function()
