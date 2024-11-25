print(set([1,2,3]))
print(set([1,2,3,3,3,1]))

print(set((1,2)))
print(set((1,2,2,1,2,2)))

print(set("absbsabcbbbcb"))
print(set({"key":"value"}))

philosophers = ["Plato", "socrates", "Plato", "Pythagoras", "socrates"]
philosophers_set = set(philosophers)

philosophers_list = list(philosophers_set)
print(philosophers_list)