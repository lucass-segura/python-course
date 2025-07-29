def deposit(balance, amount=0):
    return balance + amount

def withdraw(balance, amount=0):
    if balance > amount:
        return None

    return balance - amount

def default(*args, **kwargs):
    print('Opción no válida')

#func1 = deposit
#func2 = withdraw

#print(func1(100,10))
#print(func2(100, 102))

options = {
    '1': deposit,
    '2': withdraw,
}

option = input('Ingresa una opción - 1: deposito, 2: retiro\n')
balance = int(input('Ingresa tu balance: '))
amount = int(input('Ingresa el monto: '))

function = options.get(option, default)
total = function(balance, amount)
if total is not None:
    print(f'Tu nuevo balance es: {total}')