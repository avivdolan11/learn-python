# pillows = {
#     "soft": 79.99,
#     "hard": 99.99
# }

# print(pillows["soft"])
# print(pillows.__getitem__("soft"))

class Crayon():
    def __init__(self):
        self.crayons = []

    def add(self,crayon):
        self.crayons.append(crayon)

    def __getitem__(self, index):
        return self.crayons[index]
    
    def __setitem__(self, index, value):
        self.crayons[index] = value



cb = Crayon()
cb.add("Blue")
cb.add("Red")

print(cb[0])

cb[0] = "Yellow"

print(cb[0])

## EXAMPLE

class Car():
    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year

class Dealership():
    def __init__(self):
        self.cars = []
    
    def accept_delivery(self, car):
        self.cars.append(car)
    
    def __getitem__(self, index):
        return self.cars[index]
    
    def __setitem__(self, index, value):
        self.cars[index] = value

f150 = Car(maker = "Ford", model = "F-150", year = 2019)
camry = Car(maker = "Toyota", model = "Camry", year = 2020)
porsche = Car (maker = "Porsche", model = "911 Carrera", year = 2021)

dealership = Dealership()

dealership.accept_delivery(f150)
dealership.accept_delivery(camry)

print(dealership[0].year) # 2019 -- the F150's year

dealership[0] = porsche

for car in dealership:
  print(car.maker) # Porsche, Toyota