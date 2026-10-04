identifier = input()

print(f'Длина: {len(identifier)}', f'Только буквы: {identifier.isalpha()}', f'Только цифры: {identifier.isdigit()}', f'Буквенно-цифровая: {identifier.isalnum()}', 
      f'Содержит дефис: {'-' in identifier}', sep='\n')
