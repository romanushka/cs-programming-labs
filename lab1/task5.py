distance = float(input())
fuel_consumption = float(input())
cost_1_liter = float(input())

amount_of_fuel = (fuel_consumption * distance) / 100
fuel_cost = amount_of_fuel * cost_1_liter

print(f'Топливо: {amount_of_fuel:.2f} л' , f'Стоимость: {fuel_cost:.2f} руб', sep='\n')

# :.2f - показать дробное число с двумя знаками после запятой