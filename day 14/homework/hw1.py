#შექმენით რეგისტრაცია/ავტორიზაციის სიმულაცია:
#მომხმარებელს შემოატანინეთ ემაილი, პაროლი და შეინახეთ ისინი ცვლადებში. ისევ შემოატანინეთ ემაილი და პაროლი(ეს იქნება ავტორიზაცია) და თუ შემოტანილი მნიშვნელობები დაემთხვევა რეგისტრაციისას შეყვანლის, დაბეჭდეთ True, სხვა შემთხვევაში False.

email = input("enter your email: ")
password = input("enter your password: ")
log_in = input("enter your login email: ")
log_in1 = input("enter your login password: ")
if email == log_in and password == log_in1:
    print(True)
else:
    print(False)