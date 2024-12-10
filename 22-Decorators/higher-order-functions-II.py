def calculator(operation):
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    
    if operation == "add":
        return add
    elif operation == "subtract":
        return subtract


print(calculator("add")(10,4))
print(calculator("subtract")(10,433))

def square(num):
    return num ** 2

def cube(num):
    return num ** 3

operations = [square, cube]

for func in operations:
    print(func(5))