dinner = "steak and potatoes"

# for character in dinner:
#     print(character)

numbers = [2, 3, 7, 9, 4]

for number in numbers:
    print(number*number)


novelists = ["Fitz", "stein", "rowling"]

for novelist in novelists:
    print(len(novelist))


print(novelist)
print(number)


total = 0

for number in numbers:
    total = total + number

print(total)


def sum_of_lengths(strings):
    total = 0
    for string in strings:
        total = total + len(string)
    return total    


def product(numbers):
    total = 1
    for number in numbers:
        total = total*number
    return total   