current_temperature = float(input())
desired_temperature = float(input())

if current_temperature > desired_temperature:
    print('Охлаждение')

elif current_temperature < desired_temperature:
    print('Нагрев')

else:
    print('Выключен')