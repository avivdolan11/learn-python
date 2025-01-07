class Store():
    def __init__(self):
        self.owner = "Aviv"

    def exclaim(self):
        return "Lots of stuff to buy"

class CoffeeShop(Store):
    pass

starbucks = CoffeeShop()

print(starbucks.owner)
print(starbucks.exclaim())