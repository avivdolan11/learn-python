print(["abcdefghijklmnopqrstuvwxyz".index(char) for char in "donut"])

print([number /2 for number in range(20)])

donuts = [
    "Boston Cream",
    "Jelly",
    "Glazed",
    "Vanilla Cream"
]

creamy_donuts = []

for donut in donuts:
    if "Cream" in donut:
        creamy_donuts.append(donut)

print(creamy_donuts)

creamy_donuts = [donut for donut in donuts if "Cream" in donut]
print(creamy_donuts)

values = ["3.14", "9.99", "567.324", "5.678"]
floats = [float(value) for value in values]
print(floats)


def destroy_elements(first, second):
    return [element for element in first if element not in second]