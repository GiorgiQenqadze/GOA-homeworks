#შექმენით ფუნქცია, რომელიც იღებს სიას და აბრუნებს ამ სიაში უდიდეს რიცხვს




def maximum(sia):
    return max(sia)

sia = []
for i in range(5):
    ricxvi = int(input("შეიყვანე რიცხვი: "))
    sia.append(ricxvi)

print("უდიდესი რიცხვია:", maximum(sia))