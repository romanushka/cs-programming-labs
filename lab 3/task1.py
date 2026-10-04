code_doc = input()

category = code_doc[:3]
year = code_doc[4:8]
number = code_doc[9:13]

print(f'Категория: {category}', f'Год: {year}', f'Номер: {number}', f'Обратный номер: {number[::-1]}', sep="\n")