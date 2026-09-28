sec_input = int(input())

hours = sec_input // 3600
seconds_reman = sec_input % 3600
minutes = seconds_reman // 60
seconds = seconds_reman % 60

print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')