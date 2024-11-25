numbers = [4,7,3,9]

print(sorted(numbers))

salaries = {
    "executive assistant": 20,
    "CEO": 100
}

print(sorted(salaries))

wheel_count = {
    "Car": 4,
    "Truck": 2,
    "Bus": 8
}

print(sorted(wheel_count.items()))

for vehicle, count in sorted(wheel_count.items()):
    print(f"The next vehicle is a {vehicle} and it has {count} wheels")