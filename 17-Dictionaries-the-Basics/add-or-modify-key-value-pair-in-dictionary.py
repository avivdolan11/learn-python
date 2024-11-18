sports_team = {
    "Patriots": ["Brady", "Gronk", "Edelman"],
    "Giants": ["Manning", "Beckham"]
}

# print(sports_team["Steelers"])
sports_team["Steelers"] = ["Rothelsberger", "Brown"]
# print(sports_team["Steelers"])

print(sports_team)

sports_team["Giants"] = ["Manning"]
print(sports_team)


video_game = {}
# video_game = dict()

video_game["subtitles"] = True
video_game["difficulty"] = "Medium"
video_game["volume"] = 7

print(video_game)

words = ["danger", "beware", "danger"]

def count_words(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(count_words(words))