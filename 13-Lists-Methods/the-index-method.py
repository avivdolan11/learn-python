pizzas = ["Meatlovers", "Pepperoni", "Sausage", "BBQ Chicken", "Marg", "Meatlovers"]

print(pizzas.index("Pepperoni"))
print(pizzas.index("Meatlovers"))

if "olives" in pizzas:
    print(pizzas.index())


print(pizzas.index("Meatlovers", 2))




def encrypt_message(message):
    alphabet = "abcdefghijklmnopqrstuvwxyzab"
    encrypted = ""

    for i in message:
        encrypt_letter_index_position = alphabet.index(i) + 2
        encrypted += alphabet[encrypt_letter_index_position]

    return encrypted    