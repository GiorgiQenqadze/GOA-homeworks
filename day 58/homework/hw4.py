#შექმენით .join() ფუნქციის კლონი, დაასწრულეთ საკლასო დავალება ვისაც არ დაუსრულებია.



def my_join(separator, items):
    result = ""
    for i in range(len(items)):
        result += items[i]
        if i != len(items) - 1:
            result += separator
    return result

words = ["hello", "my", "world"]
print(my_join("-", words))