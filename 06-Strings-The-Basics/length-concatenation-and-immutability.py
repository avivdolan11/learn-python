print(len("Python"))
print(len("Phsansunsdua"))
print(len(""))

#print(len(4))
#print(len(421.122))

print("Aviv" + "Dolan")
print("Aviv" + " Dolan")
print("Aviv" + " " + "Dolan")

print("A" "B" "C")

print("---" * 3)

def long_word(word = ""):
    return len(word) > 7

print(long_word("yes"))

def first_longer_than_second(first = "", second = ""):
    return len(first) > len(second)