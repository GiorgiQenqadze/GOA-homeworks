#შექმენით ფუნქცია, რომელიც მიიღებს 3 რიცხვს, თქვენი დავალებაა დააბრუნოთ ამ სამი რიცხვის ნამრავლი.





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

def multiply_three_numbers(a, b, c):
    return a * b * c

print("უდიდესი რიცხვია:", find_max(12, 45, 33))
print("ასოების რაოდენობა:", count_letters("გამარჯობა!"))
print("რიცხვის კვადრატია:", square_number(7))
print("სამი რიცხვის ნამრავლია:", multiply_three_numbers(2, 3, 4))