numbers = list(map(int, input().split()))

copy = numbers.copy()

for i in range(len(copy)):
    if copy[i] < 0:
        copy[i] = 0

print(numbers, copy, sep="\n")