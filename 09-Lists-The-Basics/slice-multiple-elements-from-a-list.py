print("programming"[3:6])

muscles = ["biceps", "triceps", "deltoids"]

print(muscles[0:2])
print(muscles[:2])
print(muscles[1:3])

print(muscles[::-1])

def split_in_two(list, value):
    if value % 2 == 0:
        return list[2:]
    else:
        return list[0:2]
    

def nested_extraction(nl, value):
    return nl[value][value]    



def beginning_and_end(elements):
    if elements[0] == elements[-1]:
        return True
    else:
        return False
    

def long_word_in_collection(words, animal):
    if animal in words and len(animal) > 4:
        return True
    else:
        False    