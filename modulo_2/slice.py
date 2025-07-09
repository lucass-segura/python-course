# Indices
names = ["Agus", "Juan", "Pedro", "Maria", "Luis"]

# Slicing: [start:end:skips]
print(names[0:4]) # desde el indice 0 hasta el 4
print(names[:3]) # desde el inicio hasta el indice 3
print(names[3:]) # desde el indice 3 hasta el final
print(names[::2]) # desde el inicio hasta el final con saltos de 2 en 2
print(names[::-1]) # desde el final hasta el inicio

names_copy = names[:] # copia de la lista // Shallow copy
print(names_copy)
