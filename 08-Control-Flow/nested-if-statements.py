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




def divisble_by_three_and_four(number):
    if number % 3 == 0 and number % 4 == 0:
        return True
    else:
        return False



def string_theory(word):
    if len(word) > 3 and word[0] == "S":
        return True
    else:
        return False


print(string_theory("Star"))     