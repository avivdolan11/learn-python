import re 

pattern = re.compile("flower")

sentence = "There are a lot of flower in the flowery flower field"

print(pattern.findall(sentence))

for match in pattern.finditer(sentence):
    print(match)