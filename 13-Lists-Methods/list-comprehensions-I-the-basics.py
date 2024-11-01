numbers = [3, 4, 5, 6, 7]

# squares = []

# for number in numbers:
#     squares.append(number ** 2)

# print(squares)

squares = [number ** 2 for number in numbers]
print(squares)


rivers = ["Amazon", "nile", "Yangtze"]
print([len(river) for river in rivers])

expressions = ["LOL", "ROfL", "LMAO"]
print([expression.upper() for expression in expressions])