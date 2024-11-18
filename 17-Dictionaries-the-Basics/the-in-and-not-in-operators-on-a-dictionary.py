print("erm" in "watermelon")
print("xa" in "watermelon")

pokemon = {
    "Fire": ["Charmander", "Charmeleon", "Charizrd"],
    "Water": ["Squirtle", "Turtle"],
    "Grass": ["Bulbasuar"]
}

print("Fire" in pokemon)
print("Electric" in pokemon)

if "Zombie" in pokemon:
    print(pokemon["Zombie"])
else:
    print("Category doesnt exist")