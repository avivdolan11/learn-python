ingredient_1 = "pasta"
ingredient_2 = "meatballs"

if ingredient_1 == "pasta":
    if ingredient_2 == "meatballs":
        print("I recommend making pasta and meatballs")
    else:
        print("Make plain pasta")
else:
    print("No recommendations")


if ingredient_1 == "pasta" and ingredient_2 == "meatballs":
    print("I reccommend pasta and meatballs")
elif ingredient_1 == "pasta":
    print("Make plain pasta")
else:
    print("No recommendations")    