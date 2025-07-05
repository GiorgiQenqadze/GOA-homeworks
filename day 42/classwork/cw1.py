#შექმენით ფუნქცია, რომელიც მომხმარებელს შემოატანინებს 5 სახელს. შექმნის მისგან სახელების სიას და დაბეჭდავს მას.






def collect_names():
    names = []  
    for i in range(5):
        name = input(f"{i + 1}-ე სახელი: ")
        names.append(name)
    
    print("შენ შემოიტანე შემდეგი სახელები:")
    print(names)

collect_names()