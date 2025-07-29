# * Posición - (Tuple)
def suma(*numbers):
    return sum(numbers)

print(suma(2,5,3))

def info_club(club, country, *scores, **jugadores):
    print('Club:', club)
    print('Country:', country)

    average = sum(scores) / len(scores)
    print('Score: {:.2f}'.format(average))
    print('Players:')
    for position, name in jugadores.items():
        print(f'- {position}: {name}')

info_club('Real Madrid', 'Spain', 2, 5, 3, 3, 1, 0 ,5, player1= 'Mbappe', player2= 'Vinicius', player3= 'Kross')