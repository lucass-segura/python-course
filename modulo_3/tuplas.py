# Tupla es una estructura de datos inmutable
# No se puede modificar

settings = ("localhost", 3306, True)

print("settings:", settings)
print("type(settings):", type(settings))
# Acceso a elementos
print(settings[0])
print(settings[1])
print(settings[2])

print("\n---------\n")

settings2 = "localhost", 3306, True
print("settings2:", settings2)
print("type(settings2):", type(settings2), "\n")



