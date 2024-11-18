flight_price = {
    "New York": 199,
    "Chicago": 299,
    "San Francicso": 405
}

print(flight_price["New York"])
print(flight_price["Chicago"])

gym_membership = {
    15: ["Machines"],
    29: ["Machines", "supps"],
    55: ["Machines", "supps", "sauna"]
}

print(gym_membership[29])
print(gym_membership[55])

## Get method

print(gym_membership.get(29, ["Basic Dbs"]))
print(gym_membership.get(31, ["Basic Dbs"]))