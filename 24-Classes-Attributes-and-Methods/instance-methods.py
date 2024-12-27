class Pokemon():
    def __init__(self, name, specialty, health = 100):
        self.name = name
        self.specialty = specialty
        self.health = health

    def roar(self):
        print("ROARRR")

    def describe(self):
        print(f"I am {self.name} and my specialty is {self.specialty}")

    def take_damage(self, amount):
        self.health = self.health - amount
    

squirtle = Pokemon("Squirtle", "Water")
charmander = Pokemon(name = "Charmander", specialty= "Fire", health = 110)

squirtle.roar()
charmander.roar()

squirtle.describe()
charmander.describe()

print(squirtle.health)
squirtle.take_damage(40)
print(squirtle.health)


class Musician():
    def __init__(self, age, income):
        self.age = age
        self.income = income
    
    def enter_club(self):
        if self.age < 21:
            return "Access denied!"
        else:
            return "Access granted!"
    
    def play_show(self):
        self.income = self.income + 5

cliff = Musician(age=27, income = 0)
print(cliff.age)
print(cliff.enter_club())
print(cliff.income)
cliff.play_show()
print(cliff.income)
cliff.play_show()
print(cliff.income)