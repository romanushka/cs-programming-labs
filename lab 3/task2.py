surname, name, patronymic = input().split()

surname = surname.capitalize()
initials = name[0].upper() + '.' + patronymic[0].upper() + "."

print(surname, initials)