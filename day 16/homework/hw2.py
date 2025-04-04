#შექმენით ცვლადი, სადაც შეინახავთ თქვენს სახელს. მომხმარებელს შემოატანინეთ პაროლი და თუ ის უდრის "1234"-ს დაბეჭდეთ "Password is correct", სხვა შემთხვევაში დაბეჭდეთ "Password is incorrect"

name="giorgi"
password=1234
password1=int(input("enter password: "))

if password == password1:
    print("password is correct: ")
else:
    print("password is incorrect: ")