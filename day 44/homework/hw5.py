#დაწერე ფუნქცია, რომელიც იღებს სტრიქონს და აბრუნებს ამ სტრიქონის სიგრძეს



def string_length(text):
    return len(text)

user_input = input("შეიყვანე სტრიქონი: ")
print("სტრიქონის სიგრძეა:", string_length(user_input))