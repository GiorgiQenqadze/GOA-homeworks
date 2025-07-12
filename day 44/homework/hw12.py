#დაწერე ფუნქცია, რომელიც იღებს სიტყვების სიას და აბრუნებს სიის ყველაზე გრძელ სიტყვას. გამოიყენე ციკლი და 'len()' შედარებისთვის





def longest_word(words):
    if not words:
        return None  
    
    longest = words[0]
    for word in words[1:]:
        if len(word) > len(longest):
            longest = word
    return longest
words_list = ["apple", "banana", "cherry", "watermelon", "grape"]
print(longest_word(words_list))