def reverse(string):
    start_index = 0
    last_index = len(string) - 1
    reversed_string = ""

    while last_index >= start_index:
        reversed_string = reversed_string + string[last_index]
        last_index = last_index - 1

    return reversed_string       


print(reverse("straw"))  # warts



def factorial(number):
    if number == 1:
        return number

    return number * factorial(number - 1)    
        