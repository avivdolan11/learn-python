languages = ["Python", "Java", "R"]

lengths = { language: len(language) for language in languages}
print(lengths)

lengths = { language: len(language) for language in languages if "t" in language}
print(lengths)

word = "Supercalifragilisticexpialidoucious"

letter_counts = {letter: word.count(letter) for letter in word if letter > "j" }
print(letter_counts)