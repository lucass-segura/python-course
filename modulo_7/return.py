def division(n1, n2):
    if n1 == 0 or n2 == 0:
        return None
    return n1/n2

print(division(10,5))

def foo():
    return 'Lucas', 12, True # Tupla

# result = foo()
# print(type(result))
user, age, active = foo()

print(user, age, active)