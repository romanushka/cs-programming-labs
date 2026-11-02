n = int(input())

if n < 2:
    print('Не простое')

else:
    divider = 2
    condition = True

    while divider * divider <= n:
        if n % divider == 0:
            condition = False
            break
        divider += 1

    if condition:
        print('Простое')
    else:
        print('Не простое')