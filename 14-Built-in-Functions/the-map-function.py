numbers = [4, 8, 16, 32, 64, 120]
cubes = [number ** 3 for number in numbers]
print(cubes)

def cube(number):
    return number ** 3

print(list(map(cube,numbers)))


animals = ["Cats", "Bear", "Cheetah", "Dog"]

print(list(map(len, animals)))