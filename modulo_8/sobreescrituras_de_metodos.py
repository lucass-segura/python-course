class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if self.username == username and self.password == password:
            return True
        else:
            return False

class Admin(User):
    def __init__(self, username, password, email):
        #self.username = username
        #self.password = password
        super().__init__(username, password)
        self.email = email
    
    def send_email(self):
        print(">>> Email enviado a", self.email)

    def login(self, username, password):
        if super().login(username, password):
            self.send_email()

class Organizer(User):
    ...

admin = Admin('Admin1', '12345678', 'hola@hola.com')
organizer = Organizer('Organizer1', '87654321')

print(
    admin.login('Admin1', '12345678')
)