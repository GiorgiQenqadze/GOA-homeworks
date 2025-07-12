#დაწერე ფუნქცია, რომელიც იღებს სიას და აბრუნებს მას შებრუნებულ მდგომარეობაში



def reverse_list(my_list):
    return my_list[::-1]

user_input = input("შეიყვანე ელემენტები მძიმით გამოყოფით (მაგ: a,b,c,d): ")
user_list = user_input.split(",")
print("შებრუნებული სია:", reverse_list(user_list))