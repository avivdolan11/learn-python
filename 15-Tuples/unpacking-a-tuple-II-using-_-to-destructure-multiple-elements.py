employee = ("Bob", "Johnson", "Manager", 50)

first_name, last_name, *details = employee
print(first_name)
print(last_name)
print(details)

*names, position, age = employee

print(age)
print(position)
print(names)

first_name, *details, age = employee
print(first_name)
print(details)
print(age)