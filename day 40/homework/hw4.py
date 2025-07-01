#ასევე დაწერეთ პროგრამა, რომელიც შემოტანილ წინადადებას გადაიყვანს snake_case-ში.




sentence = input("შეიყვანეთ წინადადება: ")

snake_case = sentence.lower().replace(" ", "_")


print("snake_case ვერსიაა:", snake_case)