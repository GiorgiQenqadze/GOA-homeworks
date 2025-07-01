#გაკვეთილზე შევქმენით პროგრამა, რომელიც წინადადებას გადაიყვანს camelCase-ში. თქვენი დავალებაა დაწეროთ პროგრამა, რომელიც გააკეთებს პირიქით.






camel_case = input("შეიყვანეთ camelCase სიტყვა: ")


result = ""


for char in camel_case:
    if char.isupper():
        result += " " + char.lower()
    else:
        result += char

print("გადაყვანილი წინადადება:", result)