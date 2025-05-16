#მომხმარებელს შემოატანინეთ ასაკი და შეამოწმეთ თუ ის ნაკლებია 18-ზე მაშინ შეამოწმეთ თუ ასაკი ნაკლებია 14-ზე დაუბეჭდეთ Discount 20%, სხვა შემთხვევაში Discount 10%.







age = int(input("Enter your age: "))

if age < 18:
    if age < 14:
        print("Discount 20%")
    else:
        print("Discount 10%")
else:
    print("No discount")