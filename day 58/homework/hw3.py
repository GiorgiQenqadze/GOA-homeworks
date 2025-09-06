# შექმენით .split() ფუნქციის კლონი, დაასწრულეთ საკლასო დავალება ვისაც არ დაუსრულებია.




def my_split(text, separator=" "):
    words = []
    current_word = ""
    for char in text:
        if char == separator:
            if current_word:
                words.append(current_word)
                current_word = ""
        else:
            current_word += char
    if current_word:
        words.append(current_word)
    return words

sentence = "მე ძალიან მიყვარს პროგრამირება"
print(my_split(sentence, " "))