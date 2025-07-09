# Zip une dos tuplas

names =  ["Agus", "Juan", "Pedro"]
courses = ("Python", "JavaScript", "Java")

# list lo que hace es convertir el zip en una lista
print(list(zip(names, courses)))
# zip une ambas colecciones usando los indices

# tuple lo que hace es convertir el zip en una tupla
print(tuple(zip(names, courses)))