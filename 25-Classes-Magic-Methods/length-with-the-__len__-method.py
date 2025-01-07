import collections

Book = collections.namedtuple("Book", ["title", "author"])

animal_farm = Book("Animal Farm", "George Orwell")

class Library():
    def __init__(self, *books):
        self.books = books
        self.librarians = []

    def __len__(self):
        return len(self.books)
    

l1 = Library(animal_farm)
print(len(l1))