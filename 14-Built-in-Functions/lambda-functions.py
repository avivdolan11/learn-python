metals = ["gold", "silver", "platinum", "bronze"]

print(list(filter(lambda metal: len(metal) > 4, metals)))

print(list(filter(lambda metal: metal[0] == "p", metals)))
print(list(filter(lambda metal: "p" in metal, metals)))

print(list(map(lambda word: word.count("l") , metals)))



## TEST stuff

def right_words(words, value):
    output = []
    for word in words:
        if len(word) == value:
            output.append(word)
    
    return output

print(right_words(["cat", "rat", "spat", "dsibaa"], 3))