from unittest.mock import Mock

pizza = Mock()
print(pizza)
print(type(pizza))

pizza.size = "Large"
pizza.price = 19.99
pizza.ingredients = ["mushroom", "sausage"]

print(pizza.price)
print(pizza.anything)