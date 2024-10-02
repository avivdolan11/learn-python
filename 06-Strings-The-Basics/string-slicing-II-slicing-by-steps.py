alphabet = "abcdefghijklmnopqrstuvwxyz"

print(alphabet[0:10])
print(alphabet[0:10:2])

print(alphabet[0:26:3])
print(alphabet[:26:3])
print(alphabet[0::3])
print(alphabet[::3])

print(alphabet[4:20:5])
print(alphabet[-20:-8:5])
print(alphabet[::-3])
print(alphabet[::-1])

def last_five_characters(word):
    return word[-5:]

print(last_five_characters("rotoefe"))