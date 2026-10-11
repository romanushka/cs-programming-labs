side_1 = int(input())
side_2 = int(input())
side_3 = int(input())

if side_1 <= 0 or side_2 <= 0 or side_3 <= 0:
    if (side_1 + side_2 <= side_3) or (side_2 + side_3 <= side_1) or (side_1 + side_2 <= side_3):
        print('Треугольник не существует')
elif side_1 == side_2 == side_3:
    print('Равносторонний')
elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
    print('Равнобедренный')
else:
    print('Разносторонний')

