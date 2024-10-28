countries = ["US", "Canada", "Aus"]

print(countries)
print(len(countries))

countries.append("Japan")

print(countries)
print(len(countries))

value = 3
words = ["cat", "dog", "kangaroo", "mouse"]

def length_match(words, value):
    total = 0
    for word in words:
        if len(word) == value:
            total += 1
    
    return total

print(length_match(words, value))


def sum_from(value1, value2):
    total = 0
    for number in range(value1, value2 + 1):
        total += number

    return total    


def same_index_values(list1, list2):
    results = []
    for index, value in enumerate(list1):
        if value == list2[index]:
            results.append(index)

    return results
        