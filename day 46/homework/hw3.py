#შექმენით ფუნქცია, რომელიც იღებს 3 რიცხვს და აბრუნებს მათ საშუალო არითმეტიკულს (sum / quantity)





def sashualo(a, b, c):
    return (a + b + c) / 3

a = int(input("შეიყვანე პირველი რიცხვი: "))
b = int(input("შეიყვანე მეორე რიცხვი: "))
c = int(input("შეიყვანე მესამე რიცხვი: "))

print("საშუალო არითმეტიკულია:", sashualo(a, b, c))
