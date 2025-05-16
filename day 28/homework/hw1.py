#მომხმარებელს შემოატანინეთ 3 რიცხვი და დაითვალეთ რამდენი მათგანია 10-ზე მეტი. თუ ყველა შემოტანილი რიცხვი ათზე მეტია, დაბეჭდეთ "All the numbers that are larger than ten.", სხვა შემთხვევაში დაბეჭდეთ "Some numbers that are less than or equal to ten."






count_above_10 = 0

for i in range(3):
    number = float(input(f"Enter number {i + 1}: "))
    if number > 10:
        count_above_10 += 1

if count_above_10 == 3:
    print("All the numbers that are larger than ten.")
else:
    print("Some numbers that are less than or equal to ten.")