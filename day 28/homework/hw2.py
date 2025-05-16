#მომხმარებელს შემოატანინეთ რიცხვი და გაიგეთ არის თუ არა ეს რიცხვი მარტივი(მარტივი არის რიცხვი, რომელიც მხოლოდ 1-ზე და საკუთარ თავზე იყოფა). შემდეგ კი დაბეჭდეთ "This is prime number" თუ რიცხვი მარტივია, სხვა შემთხვევაში "This isn't prime number"






number = int(input("Enter a number: "))

if number > 1:
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print("This is prime number")
    else:
        print("This isn't prime number")
else:
    print("This isn't prime number")