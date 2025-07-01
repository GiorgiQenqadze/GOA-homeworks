#გაკვეთილზე შევქმენით პროგრამა, რომელიც წინადადებას გადაიყვანს camelCase-ში. თქვენი დავალებაა დაწეროთ პროგრამა, რომელიც გააკეთებს პირიქით.
#Input: "helloWorld" -> Output: "Hello world"





camel_case = input("შეიყვანეთ camelCase სიტყვა: ")

words = []
word = camel_case[0]  

for char in camel_case[1:]:
    if char.isupper():
        words.append(word)
        word = char.lower()
    else:
        word += char

words.append(word)


sentence = words[0].capitalize() + " " + " ".join(words[1:])

print("გადაყვანილი წინადადება:", sentence)