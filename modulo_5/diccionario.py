# clave (llave) : valor
# Las llaves no se pueden repetir
# En caso de repetirse se toma el ultimo valor de llave
# Los diccionarios son mutables
user = {
    'name': 'Lucas',
    'age': 25,
    'active': True,
    'course': [
        'Python',
        'JavaScript',
        'Java'
    ],
    'settings': (2721, True)
}

# user_name = user['name']  si no existe da error
# user_name = user.get('name')  si no existe no da error
user_password = user.get('password', 'El valor "password" no existe')
user_name = user.get('name')
print('name' in user)
print(user_password)
print(user_name)