age = 28

def fancy_func():
    age = 100
    print(age)

fancy_func()

print(age)

tax_rate = 0.06

def calculate_tax(price):
    return round(price * tax_rate, 2)

def calculate_tip(price):
    return round(price* tax_rate*3, 2)

print(calculate_tax(10))
print(calculate_tip(10))