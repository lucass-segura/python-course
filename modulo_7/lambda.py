"""
lambda <parametros>: <body> # Siempre retorna un valor.
Sirve para crear funciones anónimas en casos donde necesitamos una función simple.
"""

# add = lambda n1, n2=0: n1 + n2
# add = lambda *args: sum(args)
# print(add(10))
# print(add(10, 20, 10 ,20))

def deposit(balance, amount=0):
    return balance + amount

def withdraw(balance, amount=0):
    if balance > amount:
        return None

    return balance - amount

options = {
    '1': deposit,
    '2': withdraw,
}
option = input('Ingresa una opción - 1: deposito, 2: retiro\n')
balance = int(input('Ingresa tu balance: '))
amount = int(input('Ingresa el monto: '))

function = options.get(option, lambda *args, **kwargs: 'Opción no válida')
total = function(balance, amount)
print(total)