#მომხმარებელს შემოატანინეთ 5 რიცხვი. თქვენი დავალებაა დაითვალოთ აქედან დადებითი და უარყოფითი რიცხვები. საბოლოოდ დაბეჭდეთ შემდეგი ფორმატით:






positive_count = 0
negative_count = 0

for i in range(5):
    number = float(input(f"Enter number {i + 1}: "))
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1

print(f"Positive numbers count: {positive_count}")
print(f"Negative numbers count: {negative_count}")