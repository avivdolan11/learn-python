import collections

Book = collections.namedtuple("Book", ["title", "author"])

animal_farm = Book("Animal Farm", "George Orwell")

print(animal_farm[0])

print(animal_farm.author)