# * Posición - (Tuple)
# ** Nombres - (Dictionary)

# *args, **kwargs
def show_info(name, country, *args, champions=True, **kwargs):
    print("Club:", name)
    print("Country:", country)
    print("Champions:", champions)
    print("Players:", kwargs)
    print("Scores:", args)

show_info(
    'Real Madrid',
    'Spain',
    2, 5, 3, 3, 1, 0, 5, #*args
    player1='Mbappe', player2='Vinicius', player3='Kross' #**kwargs
)