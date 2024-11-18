## Pop removes an element

years = [1991, 1995, 2002]
years.pop(1)

print(years)

release_dates = {
    "Python":1991,
    "Ruby": 1995,
    "Java": 1995,
    "Go": 2007
}

release_dates.pop("Java")

print(release_dates)

release_dates.pop("Go")
print(release_dates)

release_dates.pop("Rust", 2000)

