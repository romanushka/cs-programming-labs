r, c = map(int, input().split())

table = []

for i in range(r):
    row = list(map(int, input().split()))
    table.append(row)

row_sums = []
column_sums = [0] * c

for i in range(r):
    row_sum = 0

    for j in range(c):
        row_sum += table[i][j]
        column_sums[j] += table[i][j]

    row_sums.append(row_sum)

print(f'Суммы строк: {row_sums}')
print(f'Суммы столбцов: {column_sums}')