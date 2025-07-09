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

# user['name'] = 'Agus'
# user['last_name'] = 'Garcia'
user.setdefault('name', 'Pepe') # Si existe la llave no la modifica
user.setdefault('id', 100) # Si no existe la llave la agrega

courses = user.get('course', [])
courses.append('C++')


user.update({
    'name': 'Agus',
    'last_name': 'Garcia',
    'courses': courses
})

del user['active']
value = user.pop('settings')

user.clear()

print( len(user) )
print( user )
print(value)

