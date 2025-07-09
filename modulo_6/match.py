score = 8

match score:
    case 10 | 9 | 8:
        print("Felicidades has promocionado")
    case 7 | 6:
        print("Felicidades haz regularizado")
    case _:
        print("No has aprobado")
