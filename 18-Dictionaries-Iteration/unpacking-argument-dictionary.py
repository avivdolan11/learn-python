def height_to_metres(feet, inches):
    total_inches = (feet*12) + inches
    return total_inches* 0.0254


print(height_to_metres(5,11))

stats = {
    "feet": 5,
    "inches": 11
}

print(height_to_metres(**stats))


def plenty_of_arguments(a, b, **kwargs):
    kwargs_sum = sum(kwargs.values())
    if (a + b + kwargs_sum) > 100:
        return True
    else:
        False

    

print(plenty_of_arguments(20, 30) )                         
# plenty_of_arguments(a = 50, b = 75)                  
# plenty_of_arguments(a = 50, b = 25, c = 50)          
# plenty_of_arguments(a = 25, b = 25, c = 25, d = 25)  
# plenty_of_arguments(a = 25, b = 25, c = 25, d = 26) 
