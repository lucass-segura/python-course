# Scope
# Dentro de una funcion no se puede sobreescribir el valor de una variable global
club = 'Barcelona' # Global

def show_info():
    #global club # Sirve para acceder a una variable global y poder modificarla
    club = 'Real Madrid' # Local
    print(club, id(club))

show_info()
print('------')
print(club, id(club))