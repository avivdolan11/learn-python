powerball_numbers = [4, 8, 15, 16, 22, 53]

def squares(numbers):
    squares = []
    for number in numbers:
        squares.append(number ** 2)

    return squares    



print(squares(powerball_numbers))


def convert_to_floats(numbers):
    floats = []

    for number in numbers:
        floats.append(float(number))

    return floats

print(convert_to_floats(powerball_numbers))    


def even_or_odd(numbers):
    logic = []

    for number in numbers:
        logic.append(number % 2 == 0)

    return logic   

print(even_or_odd(powerball_numbers)) 


def only_evens(numbers):
    evens = []
    
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
        else:
            pass
    
    return evens