count = 0
total = 0

while True:
    purchase_price = input()
    if purchase_price == 'stop':
        break
    price = int(purchase_price)
    count += 1
    total += price

if count == 0:
    print('Нет покупок')
else:
    print(f'Покупок: {count}', f'Общая стоимость: {total} руб', f'Средняя стоимость: {total // count:.2f} руб', sep='\n')
    