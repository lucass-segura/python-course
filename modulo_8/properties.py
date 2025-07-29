class User:
    def __init__(self, username, password, email, rol='user'):
        self.username = username
        self._password = password # Atributo privado, no se debe acceder directamente
        self.email = email
        self.rol = rol
    
    @property # Getter
    def password(self):
        if self.rol == 'admin':
            return self._password
        else:
            return 'No tienes permiso para ver la contraseña'

    @password.setter # Setter
    def password(self, new_password):
        self._password = new_password
        return print('Contraseña cambiada correctamente!')

user1 = User(
    username= 'Lucas', 
    password= '123456', 
    email= 'lucas@example.com',
    rol = 'admin'
)

print(user1.password)
user1.password = 'panqueque'
print(user1.password)
print(user1.__dict__)