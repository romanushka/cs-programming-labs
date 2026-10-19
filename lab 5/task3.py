n = int(input())

below_zero = 0
equal_zero = 0
above_zero = 0

for i in range(n):
    temperature = float(input())
    if temperature < 0:
        below_zero += 1
    elif temperature == 0:
        equal_zero += 1
    else:
        above_zero += 1

print(f'Ниже нуля: {below_zero}', f'Равны нулю: {equal_zero}', f'Выше нуля: {above_zero}', sep='\n')