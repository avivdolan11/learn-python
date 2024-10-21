values = [1,2,3,4,5]

# 1 *(0-1) = -1
# 2 * (1-1) = 0
# 3 * (2-1) = 3
# 4 * (3-1) = 8
# 5 * (4-1) = 15

def iteration_elements(numbers):
    total = 0
    for index, number in enumerate(numbers):
        total += number*(index - 1)
        
    return total

print(iteration_elements(values))