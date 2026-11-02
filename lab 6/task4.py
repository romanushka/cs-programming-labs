n = int(input())

if n < 0:
    print('Ошибка')
else:
    count = 0
    sum_numbers = 0

    if n == 0:
        count == 1
    else:
        while n > 0:
            digit = n % 10
            sum_numbers += digit
            count += 1
            n //= 10

    print(f'Цифр: {count}', f'Сумма цифр: {sum_numbers}', sep='\n')