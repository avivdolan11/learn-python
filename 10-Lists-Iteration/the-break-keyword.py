print(3 in [1,3,4,5])

def contains(values, target):
    found = False
    
    for value in values:
        if value == target:
            found == True
            break

    return found

print(contains([1,2,3,4,5,6], 2))    