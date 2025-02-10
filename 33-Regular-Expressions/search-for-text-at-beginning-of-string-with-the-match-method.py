import re

pattern = re.compile("flower")

match = pattern.match("a flower power")

if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())