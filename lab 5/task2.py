a = int(input())
b = int(input())

total = 0
product = 1

for number in range(a, b + 1):
    total += number
    product *= number

print(f'Сумма: {total}', f'Произведение: {product}', sep="\n")