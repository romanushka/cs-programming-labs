n = int(input())

if not(1 <= n <= 10):
    print('Ошибка')

else:
    for i in range(n):
        for j in range(n):
            if j > 0:
                print(" ", end="")
            if i > j:
                distance = i - j
            else:
                distance = j - i
            print(distance, end="")
        print()