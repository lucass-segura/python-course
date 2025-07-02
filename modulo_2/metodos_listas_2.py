names = ["Agus", "Juan", "Sofia", "Mirta"]

# Copiar lista
# copy_list = names[:] Shallow copy
copy_list = names.copy() 
print(copy_list)

# Reversar lista
# reverse_list = names[::-1]
reverse_list = names.reverse()
print(reverse_list)

# Ordenar lista
sort_list1 = names.sort() # Por defecto ordena de forma ascendente (A-Z)
sort_list2 = names.sort(reverse=True) # Por defecto ordena de forma descendente (Z-A)
print(sort_list1)
print(sort_list2)

# Ver ultimo elemento
print(names[-1])

print(names[::2])