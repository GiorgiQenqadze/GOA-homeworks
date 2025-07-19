# შექმენით ფუნქცია, რომელიც მიიღებს სიტყვას და დააბრუნებს მისი ასოების რაოდენობას.




def find_max(a, b, c):
    return max(a, b, c)

def count_letters(word):
    count = 0
    for char in word:
        if char.isalpha():
            count += 1
    return count

print("უდიდესი რიცხვია:", find_max(12, 45, 33))
print("ასოების რაოდენობა:", count_letters("გამარჯობა!"))