#შექმენით ფუნქცია, რომელიც მიიღებს რაღაც რიცხვს, ამის შემდეგ კი დააბრუნებს ამ რიცხვის კვადრატულ მნიშვნელობას.





def find_max(a, b, c):
    return max(a, b, c)

def count_letters(word):
    count = 0
    for char in word:
        if char.isalpha():
            count += 1
    return count

def square_number(n):
    return n ** 2

print("უდიდესი რიცხვია:", find_max(12, 45, 33))
print("ასოების რაოდენობა:", count_letters("გამარჯობა!"))
print("რიცხვის კვადრატია:", square_number(7))