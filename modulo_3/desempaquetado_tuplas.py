# Desempaquetado de tuplas
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

                    # Tupla
#day1, day2, day3 = "Monday", "Tuesday", "Wednesday"

# _ es una variable que se utiliza para ignorar valores
#first_day, _, _, _, _, day6, last_day = days

# * es una variable que se utiliza para desempaquetar valores
#first_day, *_, last_day = days

first_day, *sub_days, last_day = days

print(
    first_day,
    sub_days,
    last_day
)