phone = input()

phone = phone.replace("+", "")
phone = phone.replace(" ", "")
phone = phone.replace("(", "")
phone = phone.replace(")", "")
phone = phone.replace("-", "")

print(phone)