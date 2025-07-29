class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

user1 = User('Lucas', '123456', 'lucas@example.com')

user1.is_admin = True
user1.__dict__['active'] = False
print(user1.__dict__) # Ver los atributos del objeto