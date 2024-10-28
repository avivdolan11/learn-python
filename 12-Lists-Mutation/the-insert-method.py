plays = ["Hamlet", "MacBeth", "King Lear"]

plays.insert(1, "Juluis Caesar")
print(plays)

plays.insert(0, "Lebron")
print(plays)


def factors(value):
    my_factors = []

    for i in range(1, value+1):
        if value % i == 0:
            my_factors.append(i)

    return my_factors        