#შექმენით სიტყვების სია 10 ელემენტისგან. გადაუარეთ for ციკლით ამ სიას ისე, რომ დაბეჭდოთ ყოველი მე-2 ელემენტი(დაგჭირდებათ slicing-ი)




words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

for word in words[1::2]: 
    print(word)