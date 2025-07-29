def factory_operation(option):
    def deposit(balance, amount=0):
        return balance + amount

    def withdraw(balance, amount=0):
        return balance - amount
    
    default = lambda *args, **kwargs: 'Opción no valida'

    if option == '1':
        return deposit
    elif option == '2':
        return withdraw
    else:
        return default

option = input('Ingresa una opción - 1: deposito, 2: retiro\n')
func = factory_operation(option)
print(func(1000, 500))