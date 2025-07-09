# keys, values, items
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

print(
    tuple(user.keys())
)

print(
    list(user.values())
)

print(
    list(user.items())
)