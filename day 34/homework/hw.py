#შექმენით რიცხვების სია. გადაუარეთ მას for ციკლითი. შეამოწმეთ თუ რიცხვი ლუწია დაბეჭდეთ "Number is even", სხვა შემთხვევაში "Number is Odd"



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        print(f"Number {num} is even")
    else:
        print(f"Number {num} is odd")