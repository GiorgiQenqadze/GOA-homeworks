#შექმენი ფუნქცია, რომელიც მიიღებს რიცხვს, და დაბეჭდავს რიგით მე-5 ლუწ რიცხვს შემოტანილი რიცხვის შემდეგ.





def fifth_even_after(n):
    count = 0
    current = n + 1  

    while True:
        if current % 2 == 0:
            count += 1
            if count == 5:
                print("მე-5 ლუწი რიცხვი არის:", current)
                break
        current += 1

fifth_even_after(7)