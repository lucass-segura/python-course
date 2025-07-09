names = ["Agus", "Juan"]
new_names = ["Maria", "Sofia", "Mirta"]

print(names)

# Agregar elementos al final de la lista
names.append("Facundo")
print(names)

# Insertar elementos en una posicion especifica
names.insert(1, "Lucardo")
print(names)

# Extender lista
names.extend(new_names)
print(names)

# Buscar elemento
print("Agus" in names) 

# Indice de elemento
print(names.index("Agus")) 

# Remover elemento por valor
names.remove("Facundo")
print(names)

# Remover elemento por indice
names.pop(1)
print(names)

#sumamos todos los numeros
# print(sum(numbers))

# Remover elemento y almacenarlo en una variable
ultimo_elemento = names.pop(2)
print(ultimo_elemento)
print(names)