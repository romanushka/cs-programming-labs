train, departure, destination, time, price = input().split(";")

price = float(price)

print(f'Поезд: {train}', f'Маршрут: {departure} - {destination}', f'Отправление: {time}', f'Цена: {price:.2f} руб', sep="\n")
