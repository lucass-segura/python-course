from random import randint
"""
while <condition>:
    <statement>
"""

hits = 0
number = None
random_number = randint(0, 5)

print(random_number)
while number != random_number and hits < 3:
    number= int(input('Ingresa un número: '))

    if random_number > number:
        print('El número es mayor')
    elif random_number < number:
        print('El número es menor')
    hits += 1

else:
    if number == random_number:
        print('Ganaste!')
    else:
        print('Suerte la próxima')