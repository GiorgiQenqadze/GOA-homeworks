#დაწერე ფუნქცია, რომელიც იღებს ერთ რიცხვს და აბრუნებს "Even" თუ ლუწია, ან "Odd" თუ კენტია





def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("შეიყვანე რიცხვი: "))
print(even_or_odd(num))