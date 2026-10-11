ticket_price = float(input())
passengers_age = int(input())

if ticket_price <= 0 or not(0 <= passengers_age <= 120):
    print('Ошибка')

else:
    if 0 <= passengers_age <= 5:
        final_price = ticket_price * 0.0
    elif 6 <= passengers_age <= 17:
        final_price = ticket_price * 0.5
    elif 18 <= passengers_age <= 59:
        final_price = ticket_price * 1.0
    elif 60 <= passengers_age <= 120:
        final_price = ticket_price * 0.7

    print(f'Стоимость: {final_price:.2f} руб')
    