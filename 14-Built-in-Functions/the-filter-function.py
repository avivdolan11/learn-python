animals = ["elephant", "horse", "cat", "dog"]

long_animals = [animal for animal in animals if len(animal)>4] 
print(long_animals)

def is_long_animal(animal):
    return len(animal) > 4

print(filter(is_long_animal, animals))
print(list(filter(is_long_animal, animals)))
