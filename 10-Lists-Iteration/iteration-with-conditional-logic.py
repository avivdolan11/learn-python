values = [3,6,9,12,15]
other_values = [5,10,15,20,25]

def odds_sum(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 1:
            total = total + number

    return total        

print(odds_sum(values))


def greatest_number(numbers):
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest         


def smallest_number(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest        


def concatenate(strings):
    initial = ""
    for string in strings:
        if len(string) > 2:
            inital += string
    return initial
