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


job_opening = ("Software Engineer", "New York City", 100000)

position, city, salary = job_opening
print(position)
print(city)
print(salary)