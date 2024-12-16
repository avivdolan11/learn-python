address = ["500 fifth avenue", "New York", "NY", "10036"]

print(", ".join(address))
print("".join(address))


phone_number = ["555", "22", "4335", "52"]

print("-".join(phone_number))

def word_lengths(sentence):
    words = sentence.split(" ")
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths


def cleanup(lists):
    