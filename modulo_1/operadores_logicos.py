# Operadores logicos

# and Operador AND
r = True and True
print("AND:", r)
print(type(r),"\n")

# or Operador OR
r = True or False
print("OR:", r)
print(type(r),"\n")

# not Operador NOT
r = not True
print("NOT:", r)
print(type(r),"\n")

# Ejemplo 
r = (
    (10 > 5)
    and (10 == 10)
    and (10 % 2 == 0)
    or 10 == 2
)
print("Resultado Ej 1:", r)
print(type(r),"\n")