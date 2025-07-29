# ** Nombres - (Dictionary)
def show_info(**club):
    for key, value in club.items():
        print(f'{key}: {value}')

show_info(
    name='Real Madrid',
    country='Spain',
    scores=(2, 5, 3, 3, 1, 0, 5),
    players={
        'player1': 'Mbappe',
        'player2': 'Vinicius',
        'player3': 'Kross'
    }
)