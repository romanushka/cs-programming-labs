n = int(input())

odd_elements = 0


for i in range(n):
     element = 1 #C(r, 0) = 1
     for k in range(i + 1):
        if k > 0:
            print(' ', end='')
        print(element, end='')
        if element % 2 != 0:
            odd_elements += 1
        element = element * (i - k) // (k + 1) #C(r, k + 1) = C(r, k) * (r - k) / (k + 1), где 0 <= k < r
     print()

print(f'Нечетных элементов: {odd_elements}')
