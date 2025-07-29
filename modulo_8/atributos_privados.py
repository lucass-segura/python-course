class User:
    def __init__(self, username, password, email):
        self.username = username
        # self._password = password # Atributo privado, no se debe acceder directamente
        self.__password = password # Name Mangling, para acceder a este atributo se debe usar _User__password
        self.email = email

user1 = User(
    username= 'Lucas', 
    password= '123456', 
    email= 'lucas@example.com'
)
user1.password='xd'
user1._User__password='Cambio de contraseña'
print(user1.__dict__)
