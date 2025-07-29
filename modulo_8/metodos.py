class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
    
    def say_hello(self):
        print(f'>>> Hola, soy {self.username}.')
    
    def login(self, username, password):
        if self.username == username and self.password == password:
            user1.say_hello()
            return True
        else:
            print('>>> Credenciales incorrectas.')
            return False

user1 = User('Lucas', '123456', 'lucas@example.com')
user1.login('Lucas', '123456')