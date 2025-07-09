for number in range(1, 101):
    if number % 2 != 0:
        continue

    if number == 10:
        break
    
    print(number)