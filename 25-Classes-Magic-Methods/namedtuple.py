import collections

Book = collections.namedtuple("Book", ["title", "author"])

animal_farm = Book("Animal Farm", "George Orwell")

print(animal_farm[0])

print(animal_farm.author)




GymExercise = collections.namedtuple("GymExercise", ["name", "weight", "reps"])

squat = GymExercise("squat", 265, 3)

bench = GymExercise("benchpress", 185, 5)

deadlift = GymExercise("deadlift", 225, 6)

press = GymExercise("press", 120, 8)