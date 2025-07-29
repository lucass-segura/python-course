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
    ...

class Organizer(User):
    ...

admin = Admin('Admin1', '12345678')
organizer = Organizer('Organizer1', '87654321')

print(
    organizer.login('Organizer21', '87654321')
)