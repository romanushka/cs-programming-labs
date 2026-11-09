numbers = list(map(int, input().split()))
number = int(input())

result = []

for index, value in enumerate(numbers):
    if value == number:
        result.append(index)

print(f'Индексы: {result}')