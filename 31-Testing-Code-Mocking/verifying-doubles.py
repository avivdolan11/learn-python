import unittest
from unittest.mock import MagicMock

class BurritoBowl():
    restaurant_name = "Bobo's Burritos"

    @classmethod
    def steak_special(cls):
        return cls("Steak", "White", 1)


    def __init__(self, protein, rice, guac):
        self.protein = protein
        self.rice = rice
        self.guac = guac

    def add_guac(self):
        self.guac += 1


# lunch = BurritoBowl.steak_special()
# print(lunch.guac)

class_mock = MagicMock(spec = BurritoBowl)
print(class_mock.restaurant_name)
# print(class_mock.chicken_special())

instance_mock = MagicMock(spec = BurritoBowl.steak_special())

print(instance_mock.protein)
print(instance_mock.add_guac())