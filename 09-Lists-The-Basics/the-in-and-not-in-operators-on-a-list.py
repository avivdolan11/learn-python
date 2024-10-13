print("fast" in "breakfast")
print("fast" in "dinner")


meals = ["breakfast", "lunch", "dinner"]

print("lunch" in meals)
print("dinner" in meals)
print("snack" in meals)


test_scores = [99.0, 23.5, 43.65]

print(99.90 in test_scores)
print(99 in test_scores)



print(23 not in test_scores)

if 1000 not in test_scores:
    print("Value not there")
