errands = ["gym", "lunch", 'get promoted', "sleep"]

print(enumerate(errands))
print(type(enumerate(errands)))

for index, errand in enumerate(errands):
    print(f"{errand} is number {index} on my list of things today")


for index, errand in enumerate(errands, 1): ## starts index at 1
    print(f"{errand} is number {index} on my list of things today")



def in_list(strings, word):
    for index, element in enumerate(strings):
        if element == word:
            return index
    return -1


def sum_values_indices(numbers):
    starting = 0
    for index, element in enumerate(numbers):
        starting = starting + (index+element)
    return starting        