#დაწერე ფუნქცია, რომელიც იღებს სიის ელემენტებს და აბრუნებს მათ საშუალოს


def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

user_input = input("შეიყვანე რიცხვები მძიმით გამოყოფით (მაგ: 10,20,30): ")
num_list = [int(x) for x in user_input.split(",")]

print("საშუალო არის:", average(num_list))