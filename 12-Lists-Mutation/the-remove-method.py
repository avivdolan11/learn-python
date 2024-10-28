nintendo_games = ["Zelda", "Mario", "DK", "Zelda"]

nintendo_games.remove("Zelda")

print(nintendo_games)

if "Wario" in nintendo_games:
    nintendo_games.remove("Wario")

if "Mario" in nintendo_games:
    nintendo_games.remove("Mario")    


print(nintendo_games)


def delete_all(items, target):
    while target in items:
        items.remove(target)
    return items    


def push_or_pop(values):
    results = []

    for value in values:
        if value > 5:
            results.append(value)
        else:
            results.pop()
    return results            