numbers = list(map(int, input().split()))

result = [x ** 2 for x in numbers if x > 0 and x % 2 != 0]

print(f'Квадраты: {result}')