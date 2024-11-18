film_directors = {
    "The Godfather": "Ford Coppola",
    "The Rock": "Michael Bay",
    "Goodfellas": "Martin Scorsese"
}

print(film_directors.get("Goodfellas"))
print(film_directors.get("Bad Boys", "Michael Bay"))

film_directors.setdefault("Bad Boys", "Michael Bay")

print(film_directors)