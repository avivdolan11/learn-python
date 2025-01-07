class Animal():
    def __init__(self, name):
        self.name = name
    
    def eat(self, food):
        return f"{self.name} is enjoying the {food}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed 

watson = Dog("Watson", "Retriever")
print(watson.eat("bacon"))
print(watson.name)
print(watson.breed)