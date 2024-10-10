def pos_or_neg(number):
    if number > 0:
        return "Positve"
    
    elif number < 0:
        return "Negative"
    
    elif number == 0:
        return "Its zero"
    
print(pos_or_neg(0))
print(pos_or_neg(-5))

def calculator(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a*b
    elif operation == "divide":
        return a/b
    else:
        return "I dont know what you want me to do"
    
print(calculator("multiply", 5,3))