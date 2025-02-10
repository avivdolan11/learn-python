import re

pattern = re.compile(r"\d")

sentence = "I went to the store and bought 5 apples, 4 bananas and 3 plums"

print(pattern.findall(sentence))

pattern = re.compile(r"\D")

print(pattern.findall(sentence))

# https://regex101.com/