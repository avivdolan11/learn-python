phone_number = "555 555 1234"

print(phone_number.replace(" ", "-"))
print(phone_number.replace("5", "9"))

def fancy_cleanup(words):
    return words.strip().replace("g", "z").replace(" ", "!")