# შექმენით ცარიელი სია. მომხმარებელს შემოატანინეთ 5 სახელი და ჩაამატეთ ისინი ამ სიაში. გადაურეთ ამ სიას for ციკლით, შემდეგ კი სახელის თითოეულ ასოს(დაგჭირდება 2 for ციკლით, ანუ for ციკლი მეორე for ციკლში). ასევე for ციკლების ზემოთ უნდა გქონდეთ შექმნილი კიდევ ერთი ცარიელი სია, სადაც ჩაამატებთ ასოებიდან მხოლოდ თანხმოვნებს.
#გადაურეთ მიღებულ თანხმოვნების სიას და წაშალეთ დუბლიკატები, მოიძიეთ თუ როგორ შეიძლება სიის დასორტირება, დაასროტრირეთ ის ანბანის მიხედვით და დაბეჭდეთ.



names = []

consonants = []


vowels = "aeiouAEIOU"


for _ in range(5):
    name = input("შეიყვანეთ სახელი: ")
    names.append(name)


for name in names:
    for letter in name:
        
        if letter.isalpha() and letter not in vowels:
            consonants.append(letter.lower())


unique_consonants = sorted(set(consonants))


print("განუმეორებელი თანხმოვნები ანბანის მიხედვით:", unique_consonants)