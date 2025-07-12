#დაწერე ფუნქცია, რომელიც იღებს ორ რიცხვს და აბრუნებს მათ ჯამს




def add_numbers(a, b):
    return a + b

num1 = int(input("შეიყვანე პირველი რიცხვი: "))
num2 = int(input("შეიყვანე მეორე რიცხვი: "))

result = add_numbers(num1, num2)
print("ჯამი არის:", result)