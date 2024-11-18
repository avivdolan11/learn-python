tv_shows = {
    "The X Files": {
        "Season 1": {
            "Episodes": ["Monster", "Alien"],
            "Genre": ["Science Fiction"],
            "Year": 1993
        },
        "Season 2": {
            "Episodes": ["Scary Conspiracy"],
            "Genre": ["Horror"],
            "Year": 1994
        }
    },
    "Lost": {
        "Season 1": {
            "Episodes": ["Island"],
            "Genre": ["Comedy"],
            "Year": 2003
        }
    }
}

print(tv_shows)
print(tv_shows["The X Files"])
print(tv_shows["The X Files"]["Season 1"])
print(tv_shows["The X Files"]["Season 1"]["Episodes"])
print(tv_shows["The X Files"]["Season 1"]["Episodes"][1])

print(tv_shows["The X Files"]["Season 2"]["Year"])
print(tv_shows["Lost"]["Season 1"]["Genre"])