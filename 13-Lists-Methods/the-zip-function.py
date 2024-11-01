breakfasts = ["Eggs", "cereal", "Banana"]
lunchs = ["Sushi", "chicken", "Soup"]
dinners = ["Steaks", "Meatballs", "Pasta"]

# print(zip(breakfasts, lunchs, dinners))
# print(type(zip(breakfasts, lunchs, dinners)))
# print(list(zip(breakfasts, lunchs, dinners)))

for breakfast, lunch, dinner in zip(breakfasts, lunchs, dinners):
    print(f"My meal for today was {breakfast}, {lunch}, and {dinner}")