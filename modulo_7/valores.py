def create_user(name, age, active):
    user_data = f'Name: {name} | Age: {age} | Active: {active}'
    return user_data

print(create_user(
    age = 19,
    name = 'Agustin',
    active = True
))

def calculate_total(price, tax= 0.5, discount=3):
    total = price + (price+tax) - discount
    return total

total = calculate_total(100, 0.04, 10)
print('Total: ', total)