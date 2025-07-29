def deposit(balance, amount=0):
    return balance + amount

def withdraw(balance, amount=0):
    return balance - amount

def handle_operation(callback, *args, **kwargs): # Funcion de orden superior
    print(">>> Comenzamos la operación...")
    result = callback(*args, **kwargs)
    print(result)

options = {
    '1': deposit,
    '2': withdraw,
}
option = input('Ingresa una opción - 1: deposito, 2: retiro\n')
balance = int(input('Ingresa tu balance: '))
amount = int(input('Ingresa el monto: '))

function = options.get(
    option,
    lambda *args, **kwargs: 'Opción no válida'
)

handle_operation(
    callback=function,
    balance=balance,
    amount=amount
)