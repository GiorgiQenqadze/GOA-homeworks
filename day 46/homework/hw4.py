#შექმენით ფუნქცია, რომელიც იღებს სიას და აბრუნებს ამ სიის შებრუნებულ ვერსიას





def shebruneba(sia):
    return sia[::-1]

sia = []
for i in range(5):
    ricxvi = int(input("შეიყვანე რიცხვი: "))
    sia.append(ricxvi)

print("შებრუნებული სიაა:", shebruneba(sia))