# Nuevo String
nombre = "Agustin"
apellido = "Segura"

# 1
nombre_completo = " ".join([nombre, apellido])
print(nombre_completo)

# 2
nombre_completo = "%s %s" %(nombre, apellido)
print(nombre_completo)

# 3
base = "El nombre completo es {nombre} {apellido}"
nombre_completo = base.format(nombre=nombre, apellido=apellido)
print(nombre_completo)
