"""
class <NombreClase>(): #() se usa para heredar de otra clase
    def __init__(self):
        ...
<variable> = NombreClase()
"""

class User:
    name: str
    age: int
    email: str

user1 = User()
user1.name = "Lucas"
user1.age = 20
user1.email = "lucas@example.com"

print(user1.name)
print(user1.age)
print(user1.email)
