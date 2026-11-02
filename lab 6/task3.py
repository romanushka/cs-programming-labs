n = int(input())

if n < 2:
    print('Ошибка')

else:
    divider = 2
    first = True
    while divider * divider <= n:
        if n % divider == 0:
            if not first:
                print(" ", end="")
            print(divider, end="")
            first = False
            n //= divider
        else:
            divider += 1
    if n > 1:
        if not first:
            print(' ', end="")
        print(n, end="")

    print()