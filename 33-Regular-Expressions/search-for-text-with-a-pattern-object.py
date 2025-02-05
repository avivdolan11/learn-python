import re

pattern = re.compile("flower")
print(type(pattern))

print(pattern.search("candy"))
match = pattern.search("a red flower in the feild")
print(type(match))

if match:
    print(match.group())
    print(match.start())
    print(match.end())