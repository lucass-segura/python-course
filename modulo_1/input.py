# Input
name = input("Ingrese su nombre: ")
print("Hola", name)

# Ejemplo
first_name = str(input("\nIngrese su nombre: ")) #str
age = int(input("Ingrese su edad: ")) #int
status = input("Tu usuario se encuentra activo? (si/no): ") == "si" #bool

print("\nNombre:", first_name)
print("Edad:", age)
print("Status:", status)
print("Nombre:", type(first_name), "Edad:", type(age), "Status:", type(status))

print(
    str("10"),
    type(str("10"))
)
