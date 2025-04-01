class Book():
    def __init__(self, title, author, price = 14.99):
        self.title = title
        self.author = author
        self.price = price

animal_farm = Book("Animal Farm", "George Orwell", 20)
gatsby = Book("The Great Gatsby", "Scott F")

print(animal_farm.price)
print(gatsby.price)



class Zombie():
    def __init__(self, health = 100, brains_eaten=5):
        self.health = health
        self.brains_eaten = brains_eaten